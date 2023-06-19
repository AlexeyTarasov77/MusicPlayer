from music_commands import * # імпортуємо всі файли у папці music_commands
from paths import get_full_path # імпортуємо функцію get_full_path з папки paths
from gui_commands import place_music_name, handle_music_len, current_music_time # імпортуємо функції place_music_name та handle_music_len з папки gui_commands

from status import * # імпортуємо модуль status
import player # імпортуємо модуль player
import pygame # імпортуємо pygame

# ініціалізація
pygame.mixer.init() # ініціалізуємо mixer у pygame

# функція для скіпу та використовується у функціоналі кнопок next та prev (previous)
def skip_music(index):
    if state.is_loaded: # перевіряємо чи загружений трек
        pygame.mixer.music.unload() # вигружаємо трек
    
    # працюємо з ім'ям треку
    music_path = get_full_path(f"resources/music/{added_music[index]}") # записуємо повний шлях у змінну music_path
    player.main_app.CURRENT_MUSIC_PATH = music_path
    player.main_app.CURRENT_MUSIC_LEN = handle_music_len(pygame.mixer.Sound(music_path).get_length())
    player.main_app.CURRENT_SONG_NAME = handle_music_name(added_music[index]) # додаємо ім'я до властивості CURRENT_SONG_NAME
    place_music_name() # визиваємо функцію place_music_name (яка розміщує лейбл з ім'ям треку який зараз грає)
    # працюємо з самим треком
    state.on_load()
    pygame.mixer.music.load(music_path) # загружаємо трек
    pygame.mixer.music.play() # починаємо його гру
    current_music_time()