import time
from similarity_dispatcher import run_similarity

# Compute similarities for a chunk of function pairs
def evaluate_pairs(metric, df_chunk, src_path, log_path):
    results = []
    with open(log_path, "a") as log:
        for _, row in df_chunk.iterrows():
            try:
                f1 = f"{src_path}{row.FunID1}.java"
                f2 = f"{src_path}{row.FunID2}.java"
                results.append(run_similarity(metric, f1, f2))
            except Exception as e:
                # Log errors without stopping execution
                log.write(f"{time.asctime()} {metric} {e}\n")
                results.append(0)
    return results
