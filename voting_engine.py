import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import precision_score, recall_score, f1_score
from model_factory import build_model

# Original voting logic (strictly preserved)
def voting(vectors, labels, n):
    X = np.array(vectors)
    Y = np.array(labels)
    kf = KFold(n_splits=5)

    Precisions, Recalls, F1s = [], [], []

    for train_idx, test_idx in kf.split(X):
        train_X, train_Y = X[train_idx], Y[train_idx]
        test_X, test_Y = X[test_idx], Y[test_idx]

        preds = []

        for name in [
            "KNN_5", "KNN_1", "KNN_3",
            "DT", "ADABOOST", "GBDT",
            "RF", "LR", "XGBOOST"
        ]:
            clf = build_model(name, 256)
            clf.fit(train_X, train_Y)
            preds.append(clf.predict(test_X))

        preds = np.array(preds)
        y_pred = (preds.sum(axis=0) >= n).astype(int)

        Precisions.append(precision_score(test_Y, y_pred))
        Recalls.append(recall_score(test_Y, y_pred))
        F1s.append(f1_score(test_Y, y_pred))

    print("Voting result:")
    print(sum(F1s)/len(F1s), sum(Precisions)/len(Precisions), sum(Recalls)/len(Recalls))
