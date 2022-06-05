import os
from os.path import exists
from PIL import Image

def check_if_dir_exists():
    if exists("extracted_hiragana"):
        print("Directory 'extracted_hiragana' already exists.")
        quit()

def extract_hiragana(files):
    os.mkdir("extracted_hiragana")

    i = 0

    for file in files:
        with Image.open(file + ".png") as image:
            for y in range(40):
                for x in range(50):
                    width, height = image.size
                    sample_width = width // 50
                    sample_height = height // 40
                    sample = image.crop((x * sample_width, y * sample_height, (x + 1) * sample_width, (y + 1) * sample_height))
                    sample.save("extracted_hiragana/" + format(i, "05d") + ".png");
                    i = i + 1

if __name__ == "__main__":
    files = ["extracted/ETL8B2C1_00", "extracted/ETL8B2C1_01", "extracted/ETL8B2C1_02", "extracted/ETL8B2C1_03", "extracted/ETL8B2C1_04", "extracted/ETL8B2C1_05"]

    check_if_dir_exists()
    extract_hiragana(files)

