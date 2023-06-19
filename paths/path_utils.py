import os

def get_full_path(relative_path): # знаходження повного шляху до файлу
    return os.path.abspath(relative_path)
    