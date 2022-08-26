from PIL import Image
from common import *

input_dir = "extracted"
output_dir = "extracted_hiragana"

def extract_hiragana(files):
    i = 0

    for file in files:
        with Image.open(input_dir + "/" + file + ".png") as image:
            for y in range(40):
                for x in range(50):
                    width, height = image.size
                    sample_width = width // 50
                    sample_height = height // 40
                    sample = image.crop((x * sample_width, y * sample_height, (x + 1) * sample_width, (y + 1) * sample_height))
                    sample.save(output_dir + "/" + format(i, "05d") + ".png");
                    i = i + 1

if __name__ == "__main__":
    files = ["ETL8B2C1_00", "ETL8B2C1_01", "ETL8B2C1_02", "ETL8B2C1_03", "ETL8B2C1_04", "ETL8B2C1_05"]

    quit_if_dir_exists(output_dir)
    mkdir(output_dir)
    extract_hiragana(files)

