from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

# Create ML model based on identifier
def build_model(name, depth):
    if name == "KNN_5":
        return KNeighborsClassifier(n_neighbors=5)
    if name == "KNN_1":
        return KNeighborsClassifier(n_neighbors=1)
    if name == "KNN_3":
        return KNeighborsClassifier(n_neighbors=3)
    if name == "DT":
        return DecisionTreeClassifier(max_depth=depth)
    if name == "ADABOOST":
        return AdaBoostClassifier(
            DecisionTreeClassifier(max_depth=depth),
            random_state=0
        )
    if name == "GBDT":
        return GradientBoostingClassifier(max_depth=depth, random_state=0)
    if name == "RF":
        return RandomForestClassifier(max_depth=depth, random_state=0)
    if name == "LR":
        return LogisticRegression()
    if name == "XGBOOST":
        return XGBClassifier(max_depth=depth, random_state=0)

    raise ValueError("Unknown model type")
