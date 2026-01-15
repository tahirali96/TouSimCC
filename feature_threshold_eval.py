import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score
from xgboost import XGBClassifier
from dataset_utils import obtain_dataset, random_features

# Strict restoration of evaluate_feature_performance()
def evaluate_feature_performance():
    dir_path = "C:/Users/Shiwei/work/work2/Toma-main/output_16_sim/"
    Vectors, Labels = obtain_dataset(dir_path)
    vectors, labels = random_features(Vectors, Labels)

    X = np.array(vectors)
    y = np.array(labels)

    feature_names = [
        'Jaccard','Dice','Jaro','Jaro_winkler',
        'Levenshtein_sim','Levenshtein_ratio',
        'Bag_of_word','Fuzzy','LCS','Ngram',
        'TFIDF','AST','RollingHash','GST',
        'Semantic','Winnow'
    ]

    common_thresholds = [0.7, 0.8, 0.9]
    levenshtein_thresholds = [150, 100, 50]

    for i, name in enumerate(feature_names):
        print("Evaluating:", name)

        if name in ['Levenshtein_sim', 'GST']:
            for t in levenshtein_thresholds:
                y_pred = (X[:, i] <= t).astype(int)
                print(t,
                      precision_score(y, y_pred),
                      recall_score(y, y_pred),
                      f1_score(y, y_pred))
        else:
            clf = XGBClassifier(max_depth=16, random_state=0)
            clf.fit(X[:, i].reshape(-1,1), y)
            probs = clf.predict_proba(X[:, i].reshape(-1,1))[:,1]

            for t in common_thresholds:
                y_pred = (probs >= t).astype(int)
                print(t,
                      precision_score(y, y_pred),
                      recall_score(y, y_pred),
                      f1_score(y, y_pred))
        print()
