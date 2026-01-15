from tokenizer_core import extract_lexical_stream
import similarity_kernels as sk

# Map tool IDs to similarity functions
SIM_MAP = {
    "t1": sk.sim_jaccard,
    "t2": sk.sim_dice,
    "t3": sk.sim_jaro,
    "t4": sk.sim_jaro_winkler,
    "t5": sk.sim_levenshtein_distance,
    "t6": sk.sim_levenshtein_ratio,
    "t7": sk.sim_bow_cosine,
    "t8": sk.sim_fuzzy_match,
    "t9": sk.sim_lcs,
    "t10": sk.sim_ngram,
    "t11": sk.sim_tfidf,
    "t12": sk.sim_ast,
    "t13": sk.sim_rolling_hash,
    "t14": sk.sim_greedy_tiling,
    "t15": sk.sim_semantic_clone,
    "t16": sk.sim_winnow
}

# Load files, tokenize, and apply selected similarity
def run_similarity(metric_id, file_a, file_b):
    tokens_a = extract_lexical_stream(file_a)
    tokens_b = extract_lexical_stream(file_b)
    return SIM_MAP[metric_id](tokens_a, tokens_b)
