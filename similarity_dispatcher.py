from tokenizer_core import extract_lexical_stream
import similarity_kernels as sk
from collections import Counter

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

# Define which metric IDs expect which input type
# "tokens" -> list of tokens
# "string" -> joined string
# "counter" -> Counter object
INPUT_TYPE = {
    # token/counter based
    "t1": "tokens",
    "t2": "tokens",
    "t7": "tokens",
    "t10": "tokens",
    "t12": "tokens",
    "t13": "tokens",
    "t14": "tokens",
    "t16": "tokens",
    # string-based
    "t3": "string",
    "t4": "string",
    "t5": "string",
    "t6": "string",
    "t8": "string",
    "t9": "string",
    "t11": "string",
    "t15": "string",
}

# Normalize inputs into commonly-used representations
def normalize_inputs(tokens_a, tokens_b):
    s_a = " ".join(tokens_a)
    s_b = " ".join(tokens_b)
    c_a = Counter(tokens_a)
    c_b = Counter(tokens_b)
    return {"tokens": (tokens_a, tokens_b), "string": (s_a, s_b), "counter": (c_a, c_b)}

# Load files, tokenize, and apply selected similarity
def run_similarity(metric_id, file_a, file_b):
    tokens_a = extract_lexical_stream(file_a)
    tokens_b = extract_lexical_stream(file_b)
    norm = normalize_inputs(tokens_a, tokens_b)
    func = SIM_MAP.get(metric_id)
    if func is None:
        raise KeyError(f"Unknown metric id: {metric_id}")
    typ = INPUT_TYPE.get(metric_id, "tokens")
    a, b = norm[typ]
    return func(a, b)
