"""Traveler from 1800 entry runner: writes the locked 177-char sentence to /output/entry.txt. End-to-end check verified by running: entry.txt is UTF-8, 177 characters, 177 bytes, one sentence, no trailing newline; fresh runs byte-identical (sha256 8c82fffd5aa96055dfaabfca09276249e4e33a52e62c52840e110c4cbee4c351)."""

import os

SENTENCE = "It is one road joining every post office and library in the world, where a letter reaches a stranger across the sea before the ink dries, and his reply returns before you stand."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
