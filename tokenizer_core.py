import javalang

# Read a Java file and convert it into a sequence of tokens
# All identifiers are replaced by a generic "id"
def extract_lexical_stream(java_file_path: str):
    token_buffer = []

    # Open source file safely (ignore encoding issues)
    with open(java_file_path, "r", encoding="utf-8", errors="ignore") as src:
        for line in src:
            # Tokenize each line using Java tokenizer
            for token in javalang.tokenizer.tokenize(line):
                # Normalize variable and method names
                if isinstance(token, javalang.tokenizer.Identifier):
                    token_buffer.append("id")
                else:
                    token_buffer.append(token.value)

    return token_buffer
