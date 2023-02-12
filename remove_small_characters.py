from common import *
import shutil

input_dir = "unified_hiragana"
output_dir = "unified_hiragana_no_small"
hiragana_labels_file = "hiragana_labels.txt"
hiragana_no_small_labels_file = "hiragana_no_small_labels.txt"

small_hiraganas = ['っ', 'ゃ', 'ゅ', 'ょ']

def remove_small_characters():
    with open(hiragana_labels_file, 'r') as f:
        data = f.read()
    i = 0
    with open(hiragana_no_small_labels_file, 'w') as f:
        for c in data:
            if c not in small_hiraganas:
                shutil.copy(f"{input_dir}/{i:05d}.png", output_dir)
                f.write(c)
            i += 1

if __name__ == "__main__":
    quit_if_dir_exists(output_dir)
    mkdir(output_dir)
    remove_small_characters()