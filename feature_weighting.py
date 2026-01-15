import numpy as np
from xgboost import XGBClassifier
from dataset_utils import obtain_dataset, random_features

# Feature importance using XGBoost
def weight():
    dir_path = "C:/Users/Shiwei/work/work2/Toma-main/output_16_sim/"
    Vectors, Labels = obtain_dataset(dir_path)
    vectors, labels = random_features(Vectors, Labels)

    X = np.array(vectors)
    y = np.array(labels)

    model = XGBClassifier(max_depth=16, random_state=0)
    model.fit(X, y)

    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    feat_labels = [
        'Jaccard','Dice','Jaro','Jaro_winkler',
        'Lev_sim','Lev_ratio','BoW','Fuzzy',
        'LCS','Ngram','TFIDF','AST',
        'RollingHash','GST','Semantic','Winnow'
    ]

    for i in range(len(indices)):
        print(f"{i+1:2d}) {feat_labels[indices[i]]:20s} {importances[indices[i]]:.6f}")
