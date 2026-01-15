import time
import math
import pandas as pd
import multiprocessing as mp
from functools import partial
from tqdm import tqdm
from parallel_executor import evaluate_pairs

# Split dataframe for parallel processing
def split_dataframe(df, parts):
    size = math.floor(len(df) / parts)
    return [
        df[i*size:(i+1)*size] if i < parts-1 else df[i*size:]
        for i in range(parts)
    ]

def main():
    # Input paths
    csv_file = "PATH/type-2.csv"
    src_path = "PATH/id2sourcecode/"
    log_path = "PATH/errorlog.txt"

    # Load clone pairs
    pairs = pd.read_csv(csv_file, header=None).drop(0)
    pairs.columns = ["FunID1", "FunID2", "x", "y", "z"]
    pairs = pairs[["FunID1", "FunID2"]]

    # Split work for multiprocessing
    chunks = split_dataframe(pairs, 60)

    metrics = [f"t{i}" for i in range(1, 17)]
    results = {}

    # Run each similarity metric
    for m in metrics:
        worker = partial(evaluate_pairs, m, src_path=src_path, log_path=log_path)
        pool = mp.Pool(60)

        scores = []
        for out in tqdm(pool.imap(worker, chunks)):
            scores.extend(out)

        pool.close()
        pool.join()
        results[m] = scores

    # Save results
    final = {"FunID1": pairs.FunID1.tolist(), "FunID2": pairs.FunID2.tolist()}
    for m in metrics:
        final[f"{m}_sim"] = results[m]

    pd.DataFrame(final).to_csv("PATH/output_16_sim/result.csv", index=False)

if __name__ == "__main__":
    start = time.time()
    main()
    print("Execution time:", time.time() - start)
