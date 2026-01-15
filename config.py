import argparse

# Parse command-line arguments (kept for full compatibility)
def parse_options():
    parser = argparse.ArgumentParser(description="Clone Classification")
    parser.add_argument(
        "-d", "--dir",
        help="Directory containing feature CSV files",
        required=True,
        type=str
    )
    parser.add_argument(
        "-o", "--out",
        help="Output directory",
        required=True,
        type=str
    )
    return parser.parse_args()
