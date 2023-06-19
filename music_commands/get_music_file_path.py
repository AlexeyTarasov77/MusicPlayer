from customtkinter import filedialog
import pygame

pygame.mixer.init()

# функция поиска пути к файлам музыки и его сохранения
def get_music_file_path():
    try:
        with filedialog.askopenfile(mode = 'r', filetypes = [('MP3 Files', '*.mp3')]) as music_file:
            if pygame.mixer.Sound(music_file.name).get_length() > 1:
                return music_file.name
            else:
                raise TypeError

    except TypeError:
        pass