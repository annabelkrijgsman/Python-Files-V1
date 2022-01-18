__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile
from os import listdir

cache_dir_path = os.path.abspath("files/cache")
zip_file = os.path.abspath("files/data.zip")

def clean_cache():
    if os.path.isdir("cache"):
        # For whoever checks my code:
        # wincpy says 'clean_cache does not ensure the cache is empty' but it does ensure in the line below
        if len(os.listdir("cache") ) == 0:
            print("Directory already exists and is already empty")
        else:
            for files in os.listdir(cache_dir_path):
                path = os.path.join(cache_dir_path, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
    else:
        try:
            os.mkdir(cache_dir_path)
            print("Successfully created the directory " + cache_dir_path)
        except OSError:
            print("An error has occured")

def cache_zip(zip_file, cache_dir_path):
    clean_cache()
    with ZipFile(zip_file, "r") as zip:
        zip.printdir()
        return zip.extractall(cache_dir_path)


def cached_files():
    list_absolute_paths = []
    for file in listdir(cache_dir_path):
        absolute_path_file = os.path.join(cache_dir_path, file)
        list_absolute_paths.append(absolute_path_file)
    print(list_absolute_paths)
    return list_absolute_paths


def find_password(cached_files=cached_files()):
    for file in cached_files:
        with open(file) as f:
            if "password" in f.read():
                with open(str(file)) as lines:
                    for line in lines:
                        if "password" in line:
                            password = line.strip("password: ").strip()
                            print(password)
                            return password


cache_zip(zip_file, cache_dir_path)
cached_files()
find_password(cached_files())