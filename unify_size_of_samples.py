from PIL import Image
from common import *

input_dir = "clean_hiragana"
output_dir = "unified_hiragana"

def unify_samples():
    for f in os.listdir(input_dir):
        if os.path.isfile(f"{input_dir}/{f}") and f.endswith(".png"):
            with Image.open(f"{input_dir}/{f}") as image:
                unify_sample(image).save(f"{output_dir}/{f}")

if __name__ == "__main__":
    quit_if_dir_exists(output_dir)
    mkdir(output_dir)
    unify_samples()

