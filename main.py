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
