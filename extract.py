import os
import shutil
from os import listdir
from os.path import exists

def check_if_dir_exists():
    if exists("extracted"):
        print("Directory 'extracted' already exists.")
        quit()

def create_file_list(etl_dirs, files):
    for dir in etl_dirs:
        for f in listdir(dir):
            if f.startswith("ETL") and not f.endswith("INFO"):
                files.append(dir + "/" + f)

def extract_files(files):
    for f in files:
        print("Extracting " + f + "...")
        os.system("python3 unpack.py " + f)
        print("Extracted " + f)

def create_extracted_file_list(etl_dirs, files):
    files.clear()
    for dir in etl_dirs:
        for f in listdir(dir):
            if f.endswith(".png") or f.endswith(".txt") or f.endswith(".csv"):
                files.append(dir + "/" + f)

def move_extracted_files_to_dedicated_dir(files):
    os.mkdir("extracted")

    print("Moving files to 'extracted' directory...")

    for f in files:
        shutil.move(f, "extracted")

if __name__ == "__main__":
    etl_dirs = ["ETL/ETL1", "ETL/ETL2", "ETL/ETL3", "ETL/ETL4", "ETL/ETL5", "ETL/ETL6", "ETL/ETL7", "ETL/ETL8B", "ETL/ETL8G", "ETL/ETL9B", "ETL/ETL9G"]
    files = []

    check_if_dir_exists()
    create_file_list(etl_dirs, files)
    extract_files(files)
    create_extracted_file_list(etl_dirs, files)
    move_extracted_files_to_dedicated_dir(files)

