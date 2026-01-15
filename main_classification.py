import time
from dataset_utils import obtain_dataset, random_features
from voting_engine import voting
from xgboost_runner import XGBoost
from feature_weighting import weight
from feature_threshold_eval import evaluate_feature_performance
from parameter_tuning import parameters

def main1():
    dir_path = "C:\Projects\TouSimCC/output_16_sim/"
    Vectors, Labels = obtain_dataset(dir_path)
    vectors, labels = random_features(Vectors, Labels)

    start = time.time()
    XGBoost(vectors, labels)
    print("Elapsed:", time.time() - start)

if __name__ == "__main__":
    evaluate_feature_performance()
    main1()
    weight()
    parameters()
