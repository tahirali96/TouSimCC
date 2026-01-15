import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
from model_factory import build_model
from dataset_utils import obtain_dataset, random_features

# Strict restoration of parameter testing
def parameters():
    dir_path = "C:/Users/Shiwei/work/work2/Toma-main/output_16_sim/"
    Vectors, Labels = obtain_dataset(dir_path)
    vectors, labels = random_features(Vectors, Labels)

    X = np.array(vectors)
    Y = np.array(labels)

    depths = [8,16,32,64,128,256]
    kf = KFold(n_splits=5)

    for train_idx, test_idx in kf.split(X):
        train_X, train_Y = X[train_idx], Y[train_idx]
        test_X, test_Y = X[test_idx], Y[test_idx]

        for d in depths:
            for name in ["XGBOOST","RF","DT","ADABOOST","GBDT"]:
                model = build_model(name, d)
                model.fit(train_X, train_Y)
                pred = model.predict(test_X)
                print(name, d, f1_score(test_Y, pred))
        break
