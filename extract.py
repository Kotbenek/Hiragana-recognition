import os
import shutil
from os import listdir
from os.path import exists

etl_dirs = ["ETL/ETL1", "ETL/ETL2", "ETL/ETL3", "ETL/ETL4", "ETL/ETL5", "ETL/ETL6", "ETL/ETL7", "ETL/ETL8B", "ETL/ETL8G", "ETL/ETL9B", "ETL/ETL9G"]
files = []

if exists("extracted"):
    print("Directory 'extracted' already exists.")
    quit()

for dir in etl_dirs:
    for f in listdir(dir):
        if f.startswith("ETL") and not f.endswith("INFO"):
            files.append(dir + "/" + f)

for f in files:
    print("Extracting " + f + "...")
    os.system("python3 unpack.py " + f)
    print("Extracted " + f)

files = []
for dir in etl_dirs:
    for f in listdir(dir):
        if f.endswith(".png") or f.endswith(".txt") or f.endswith(".csv"):
            files.append(dir + "/" + f)

os.mkdir("extracted")

print("Moving files to 'extracted' directory...")

for f in files:
    shutil.move(f, "extracted")

