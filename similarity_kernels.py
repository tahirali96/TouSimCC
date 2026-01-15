import math
import re
import difflib
import numpy as np
from collections import Counter
from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
import Levenshtein
from pygments import lex
from pygments.lexers import JavaLexer

# Count common and total token occurrences
def _count_intersection_union(seq1, seq2):
    c1, c2 = Counter(seq1), Counter(seq2)
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    return intersection, union

##### Basic similarity metrics

# Jaccard similarity using token frequency
def sim_jaccard(seq1, seq2):
    i, u = _count_intersection_union(seq1, seq2)
    return i / u if u else 0.0

# Dice similarity (overlap weighted)
def sim_dice(seq1, seq2):
    i, _ = _count_intersection_union(seq1, seq2)
    return (2 * i) / (len(seq1) + len(seq2)) if (seq1 or seq2) else 0.0

# Character-level Jaro similarity
def sim_jaro(seq1, seq2):
    return Levenshtein.jaro(seq1, seq2)

# Improved Jaro similarity with prefix boost
def sim_jaro_winkler(seq1, seq2):
    return Levenshtein.jaro_winkler(seq1, seq2)

##### Edit-distance based

# Raw Levenshtein edit distance
def sim_levenshtein_distance(seq1, seq2):
    return Levenshtein.distance(seq1, seq2)

# Normalized Levenshtein similarity
def sim_levenshtein_ratio(seq1, seq2):
    return Levenshtein.ratio(seq1, seq2)

##### Vector and fuzzy matching

# Cosine similarity using bag-of-words
def sim_bow_cosine(seq1, seq2):
    c1, c2 = Counter(seq1), Counter(seq2)
    vocab = set(c1) | set(c2)
    v1 = [c1.get(w, 0) for w in vocab]
    v2 = [c2.get(w, 0) for w in vocab]

    dot = sum(x * y for x, y in zip(v1, v2))
    mag = math.sqrt(sum(x*x for x in v1)) * math.sqrt(sum(y*y for y in v2))
    return dot / mag if mag else 0.0

# Fuzzy string matching similarity
def sim_fuzzy_match(seq1, seq2):
    return fuzz.ratio(" ".join(seq1), " ".join(seq2)) / 100.0

##### Structural similarity

# Longest Common Subsequence similarity
def sim_lcs(seq1, seq2):
    s1, s2 = " ".join(seq1), " ".join(seq2)
    lcs = difflib.SequenceMatcher(None, s1, s2)\
        .find_longest_match(0, len(s1), 0, len(s2)).size
    return (2 * lcs) / (len(s1) + len(s2)) if (s1 and s2) else 0.0

###### N-gram and TF-IDF

# Token-level N-gram similarity
def sim_ngram(seq1, seq2, n=15):
    def grams(seq):
        return set(tuple(seq[i:i+n]) for i in range(len(seq)-n+1))
    g1, g2 = grams(seq1), grams(seq2)
    return len(g1 & g2) / len(g1 | g2) if (g1 | g2) else 0.0

# TF-IDF cosine similarity
def sim_tfidf(seq1, seq2):
    corpus = [" ".join(seq1), " ".join(seq2)]
    mat = TfidfVectorizer().fit_transform(corpus)
    return float(mat[0] @ mat[1].T)

##### AST-inspired and hashing

# Approximate AST similarity using Java lexer tokens
def sim_ast(seq1, seq2):
    def lex_tokens(code):
        return Counter(tok for tok, _ in lex(code, JavaLexer()))

    t1, t2 = lex_tokens(" ".join(seq1)), lex_tokens(" ".join(seq2))
    inter = sum((t1 & t2).values())
    total = sum(t1.values()) + sum(t2.values())
    return (2 * inter / total) if total else 0.0

# Rolling hash based similarity
def sim_rolling_hash(seq1, seq2, min_len=10):
    def rolling(text):
        h = 0
        for ch in text:
            h = (h * 256 + ord(ch)) % (10**9 + 7)
        return h

    s1, s2 = " ".join(seq1), " ".join(seq2)
    hashes = {rolling(s1[i:i+min_len]) for i in range(len(s1)-min_len+1)}
    matches = sum(rolling(s2[i:i+min_len]) in hashes
                  for i in range(len(s2)-min_len+1))
    return matches / (len(seq1) + len(seq2)) if (seq1 or seq2) else 0.0


##### Advanced clone detection

# Greedy string tiling similarity
def sim_greedy_tiling(seq1, seq2):
    score = 0
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            k = 0
            while i+k < len(seq1) and j+k < len(seq2) and seq1[i+k] == seq2[j+k]:
                k += 1
            score += k
    return (2 * score) / (len(seq1) + len(seq2)) if (seq1 or seq2) else 0.0

# Semantic similarity using sequence matcher
def sim_semantic_clone(seq1, seq2):
    return difflib.SequenceMatcher(
        None, " ".join(seq1), " ".join(seq2)
    ).ratio()

# Winnowing fingerprint similarity
def sim_winnow(seq1, seq2, k=5, w=10):
    def winnow(text):
        grams = [text[i:i+k] for i in range(len(text)-k+1)]
        return {
            min(hash(g) for g in grams[i:i+w])
            for i in range(len(grams)-w+1)
        }

    f1, f2 = winnow(" ".join(seq1)), winnow(" ".join(seq2))
    return len(f1 & f2) / min(len(f1), len(f2)) if (f1 and f2) else 0.0
