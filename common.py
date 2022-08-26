import os
from os.path import exists

def quit_if_dir_exists(dir):
    if exists(dir):
        print("Directory '" + dir + "' already exists.")
        quit()

def mkdir(dir):
    os.mkdir(dir)
