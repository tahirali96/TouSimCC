import csv
import random
from itertools import islice

# Read feature vectors from a CSV file
def feature_extraction_all(feature_csv):
    features = []
    with open(feature_csv, 'r') as f:
        reader = csv.reader(f)
        for row in islice(reader, 1, None):
            try:
                features.append([float(v) for v in row[2:]])
            except:
                pass
    print("len:")
    print(len(features))
    return features


# Load clone and non-clone datasets
def obtain_dataset(dir_path):
    nonclone_csv = dir_path + 'nonclone_sim.csv'
    clone_csv = dir_path + 'clone_sim.csv'

    nonclone_features = feature_extraction_all(nonclone_csv)
    clone_features = feature_extraction_all(clone_csv)

    vectors = []
    labels = []

    vectors.extend(nonclone_features)
    labels.extend([0] * len(nonclone_features))

    vectors.extend(clone_features)
    labels.extend([1] * len(clone_features))

    print("len of Vectors:")
    print(len(vectors))
    print("len of Labels:")
    print(len(labels))

    return vectors, labels


# Shuffle features and labels together
def random_features(vectors, labels):
    merged = []
    for i in range(len(vectors)):
        row = vectors[i]
        row.append(labels[i])
        merged.append(row)

    random.shuffle(merged)
    return [m[:-1] for m in merged], [m[-1] for m in merged]
