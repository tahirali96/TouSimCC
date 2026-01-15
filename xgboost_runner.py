import time
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score, precision_score, recall_score
from xgboost import XGBClassifier
import joblib

# Original XGBoost-only evaluation (with timing)
def XGBoost(vectors, labels):
    X = np.array(vectors)
    Y = np.array(labels)

    kf = KFold(n_splits=5)
    F1s, Ps, Rs = [], [], []

    for train_idx, test_idx in kf.split(X):
        train_X, train_Y = X[train_idx], Y[train_idx]
        test_X, test_Y = X[test_idx], Y[test_idx]

        start_train = time.time()
        clf = XGBClassifier(max_depth=16, random_state=0)
        clf.fit(train_X, train_Y)
        joblib.dump(clf, "clf_XGBoost.pkl")
        train_time = time.time() - start_train

        start_pred = time.time()
        y_pred = clf.predict(test_X)
        pred_time = time.time() - start_pred

        F1s.append(f1_score(test_Y, y_pred))
        Ps.append(precision_score(test_Y, y_pred))
        Rs.append(recall_score(test_Y, y_pred))

        break

    print("Training time:", train_time)
    print("Prediction time:", pred_time)
    print(sum(F1s)/len(F1s), sum(Ps)/len(Ps), sum(Rs)/len(Rs))
