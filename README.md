# TouSimCC

TouSimCC is an end-to-end pipeline that computes multiple similarity measures between Java functions, aggregates them into feature vectors, and trains machine-learning models (XGBoost and ensemble meta-classifier) to detect code clones (Type‑1 .. Type‑4). This README documents (1) what the code actually implements, (2) the experimental setup reported in the paper, (3) hyperparameter/threshold settings used in experiments, and (4) practical notes and recommendations (my observations).

## Quick summary (what the repository actually does)
- Tokenization: extracts lexical token streams from Java functions (identifier normalization applied) using `javalang` tokenizer logic in `tokenizer_core.py`.
- Similarity feature computation: computes 16 similarity measures for each function pair in `similarity_kernels.py` and orchestrates them in `similarity_dispatcher.py`.
- Parallel execution: `main_similarity.py` + `parallel_executor.py` generate pairs and compute features in parallel (writes CSV feature output).
- Dataset utilities: `dataset_utils.py` loads feature CSVs and labels and provides splitting/preprocessing helpers.
- Modeling: `xgboost_runner.py`, `model_factory.py`, and `voting_engine.py` implement single-model training (XGBoost) and a meta-classifier ensemble.
- Tuning & analysis: `parameter_tuning.py` and `feature_weighting.py` support hyperparameter search and per-feature weighting experiments.

## Datasets used (as in the paper and code)
- BigCloneBench (BCB)
  - The paper/sample experiments randomly sampled approximately 270,000 true clone pairs from BCB for experiments.
  - BCB clone-type breakdown reported (paper):
    - Moderately Type-3 (MT3) clones: 86,341
    - Strong Type-3 (ST3) clones: 21,395
    - Type-1 clones: 48,116
    - Type-2 clones: 4,234
    - Weak Type-3/Type-4 (WT3/T4): 109,914
  - BCB also contains a large number of non-clone pairs (paper reports ~278,838 false pairs used in comparison).
- Google Code Jam (GCJ)
  - GCJ used as a complementary dataset with predominantly semantic (Type-4) clones:
    - 275,570 semantic clone pairs
    - 1,116,376 non-clone pairs
  - These datasets are used for cross-dataset evaluation and to demonstrate robustness to semantic clones.

## Similarity metrics implemented
The repository computes the following measures (as implemented in `similarity_kernels.py` and shown in the paper tables):

- L_dis (Levenshtein distance / related string metrics)
- RKR-GST (substring-based metric)
- Jaccard
- Dice
- Jaro
- Jaro-Winkler
- L_ratio (normalized edit ratio)
- B_word (bag-of-words similarity)
- f_matching (token matching heuristics)
- L_subsequence (Longest Common Subsequence ratio)
- N-grams (n-gram overlap)
- TF_IDF (TF-IDF cosine similarity)
- ASTs (AST-structural / tree-based heuristics)
- Rolling_hash (rolling-hash fingerprint overlap)
- Semantic_clone (semantic/embedding-like heuristic)
- Winnow (winnowing/fingerprint overlap)

Note: some kernels in the code expect token lists while others operate on strings or numeric counters. See "Important implementation notes" below.

## Thresholds and per-metric decision points used in experiments
The experiments in the paper and the code evaluate metric effectiveness across a set of thresholds. The important thresholds used in the reported experiments:

- Probability / similarity thresholds applied as operational cutoffs for many metrics: {0.7, 0.8, 0.9}
  - Used to binarily label a pair as "similar" for simple unsupervised evaluation of individual metrics (precision/recall/F1 reported at these thresholds).
- Raw-value thresholds (distance/score) for some string-distance methods:
  - Levenshtein-distance and RKR-GST: raw cutoffs {150, 100, 50} (these are raw-distance cutoffs, not ratios).
- Small-value thresholds for ratio-based metrics (LCS, ASTs, Winnow) used particularly on GCJ:
  - Example paper thresholds: {0.07, 0.08, 0.09} (empirical operational points used to evaluate sensitivity for low similarity scores typical of semantic clones).
- Ensemble decision rule:
  - The ensemble meta-classifier in the paper marks a pair as "clone" if at least five base classifiers predict "clone" (this majority threshold was used in their ensemble experiments).

If you run experiments from code, ensure you pass or set the threshold values explicitly (scripts use thresholds as parameters in several places).

## Machine-learning algorithms & hyperparameter ranges
The code and paper evaluate several supervised classifiers. Exact algorithms used in experiments include:
- K-nearest neighbors (KNN) — K ∈ {1, 3, 5}
- Decision Tree (DT)
- Random Forest (RF)
- AdaBoost
- Gradient Boosting Decision Tree (GBDT)
- eXtreme Gradient Boosting (XGBoost)
- Logistic Regression (LR)
- Ensemble meta-classifier (combines base classifiers)

Hyperparameter settings and search strategy reported:
- Tree depths evaluated (explicit grid): {8, 16, 32, 64, 128, 256}
  - These depths were explored to select optimal tree complexity.
- K for KNN: {1, 3, 5}
- Boosting algorithms (AdaBoost, GBDT, XGBoost): tuned with optimized hyperparameters (XGBoost was the preferred baseline for final evaluation).
- XGBoost typical parameters you will find in code/tuning:
  - n_estimators / num_boost_round (with early stopping)
  - max_depth ∈ {3..12} (or the above grid for tree-based experiments)
  - learning_rate (eta) typical ranges: 0.01–0.2
  - subsample, colsample_bytree ∈ [0.5, 1.0]
  - min_child_weight, reg_alpha, reg_lambda (regularization)
- Cross-validation:
  - Stratified K‑fold CV (k = 5) and hold-out validation are used for parameter selection and model assessment.
- Statistical tests:
  - The paper uses Kolmogorov–Smirnov (KS) tests and Wilcoxon signed-rank test to compare model outcomes (paired comparisons; significance threshold p < 0.05).

If you run parameter tuning with `parameter_tuning.py`, the script explores configurable ranges — check that script for exact parameter ranges and the chosen search method (random or grid).

## Evaluation metrics & reporting
- Per-metric and model-level evaluation metrics used in the paper and code:
  - Precision, Recall, F1-score (primary)
  - Mean(%) across various models is computed for consolidated comparison
  - In some places the paper reports PR and ROC curves and AUC-like behavior implicitly (focus remains on precision/recall/F1).
- Cross-dataset evaluation: models are compared across BCB and GCJ to show performance differences on token-like clones vs semantic clones.
- Statistical significance: Wilcoxon signed-rank / KS-test for non-normal distributions. Report p-values for pairwise model comparisons.

## Experimental environment (reported)
- Hardware: Dell Precision 7920 Tower, Intel Xeon Gold 6132 CPU, 256 GB RAM (as reported in the paper).
- Libraries used in implementation: Python + javalang tokenizer, Levenshtein module, scikit-learn, XGBoost, etc. (see `requirements.txt` for dependencies).

## Important implementation notes & observations (my findings)
These are concrete observations about the repository and how to make experiments more robust and reproducible. They reflect code behavior I inspected and practical gaps between the experiments and reproducibility:

1. Input-type consistency across kernels
   - Some similarity kernels expect string inputs (Levenshtein/jaro), others expect token lists or Counters (BOW, TF-IDF). Right now inputs are not always normalized in one place. Recommendation: normalize in the dispatcher so each kernel receives the correct type (string vs tokens vs counter).

2. Deterministic hashing for rolling-hash/winnow
   - Use a deterministic hashing function (e.g., hashlib.md5 digest sliced to int) instead of Python's builtin hash (which is randomized per process by default) to ensure reproducible fingerprints.

3. Multiprocessing defaults and resource usage
   - Several places contain hard-coded Pool sizes (e.g., 60). Change to use min(requested_workers, cpu_count()) and make workers a CLI argument.

4. Concurrent file writes and logging
   - Concurrent append to the same CSV or log file from multiple worker processes can cause interleaving/corruption. Use per-process shards and merge, or a process-safe queue+writer pattern.

5. Paths & configuration
   - Replace hard-coded absolute/Windows paths in scripts with CLI arguments or a `config.py` / .env for portability.

6. Replace fuzzywuzzy with rapidfuzz
   - rapidfuzz is faster and actively maintained; fuzzywuzzy relies on Levenshtein and can be slower.

7. Probabilities and threshold selection
   - The paper chooses thresholds empirically (grid of values) and picks the one maximizing F1 or desired metric. I recommend:
     - Use the validation set to pick threshold that maximizes chosen metric (F1, MCC, or PR-derived objective).
     - Optionally calibrate predicted probabilities (Platt or isotonic) before selecting threshold.

8. Reproducibility & metadata
   - Save experiment metadata with each result: commit SHA, parameter grid, random seeds (numpy, random, xgboost), dataset subsets, and environment details.

9. Unit tests
   - Add unit tests for each similarity kernel with small token pairs and known outputs to quickly detect regressions.

10. Pin dependency versions
   - Current `requirements.txt` lists packages but not pinned versions. Pin versions to reproduce experiments exactly.

## How to reproduce the experiments (recommended step-by-step)
1. Prepare environment:
   - Python 3.8+; pip install -r requirements.txt (pin versions recommended).
2. Tokenize functions:
   - Run any tokenizer utility or use `tokenizer_core.py` to get per-function token sequences.
3. Compute pairwise similarities:
   - Run `main_similarity.py` to produce features CSV (pass --workers, --output, etc).
4. Preprocess and split:
   - Use `dataset_utils.py` to create training/validation/test splits (stratified).
5. Train baseline XGBoost:
   - `python xgboost_runner.py --train <train.csv> --valid <valid.csv> --model-out model.joblib`
   - Use early stopping on validation and set random seeds.
6. Tune hyperparameters:
   - `python parameter_tuning.py` (configure search method — random/grid — and ranges).
7. Select decision threshold:
   - On validation set compute probabilities and select threshold that maximizes F1 or chosen metric.
8. Final evaluation:
   - Evaluate on hold-out test set. Report Precision, Recall, F1, and optionally PR/ROC curves.
9. Ensemble:
   - Train base classifiers; construct meta-classifier that aggregates base predictions; apply majority threshold (paper used 5-of-N) or learn a stacking classifier.

## Reproducibility checklist (short)
- Pin package versions in `requirements.txt`.
- Add a script to set deterministic seeds for numpy/random/xgboost.
- Use deterministic hashing for fingerprints.
- Remove hard-coded paths and provide CLI args or config.
- Use safe multiprocessing patterns for writes.
- Save metadata (commit, param grid, seed) with every experiment output.

## Additional notes from my side (not just the paper)
- The approach (computing many complementary unsupervised metrics then training a classifier) is sensible and gives high accuracy for token-level clones; it also performs reasonably on semantic clones when including semantic/AST features.
- For semantic (Type‑4) clones, reliance on TF-IDF, AST heuristics and semantic heuristics (e.g., semantic_clone) is necessary; consider adding modern vector embeddings (code2vec/CodeBERT/RoBERTa embeddings) to improve Type‑4 recall without exploding compute cost.
- Consider a hybrid setup: use cheap token-based filters to eliminate obviously non-clones, then compute heavier features (AST/embedding) only for candidate pairs to scale to very large corpora.
- If you want to reduce false positives when operating at scale, adjust the ensemble decision threshold (e.g., increase the required number of base classifiers voting "clone") or require both a high model probability and at least one high semantic score.

## Where I can help next
- Commit this README.md into the repository (default branch) or open a PR with this README + a pinned `requirements.txt`.
- Implement the input normalization fix in `similarity_dispatcher.py` so every kernel receives the correct type.
- Replace any usage of `hash()` for fingerprints with a deterministic hash.
- Add a small example end-to-end script and unit tests for each metric.
