import os
from paths import get_full_path

def get_music_names(): # получаем названия файлов музыки для фрейма 
    return os.listdir(get_full_path('resources/music'))