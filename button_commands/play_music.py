import player # імпортуємо модуль player
import pygame # імпортуємо pygame
from paths import get_full_path # імпортуємо функцію get_full_path з папки paths

from music_commands import added_music, handle_music_name # імпортуємо функції added_music та handle_music_name з папки music_commands
from status import * # імпортуємо модуль status
from gui_commands import place_music_name, place_music_len, current_music_time, handle_music_len # імпортуємо функції place_music_name, place_music_len, current_music_time 
# та handle_music_len з папки gui_commands

# ініціалізація
pygame.init() # ініціалізацуємо pygame
pygame.mixer.init() # ініціалізацуємо mixer у pygame

# функція відповідальна за початок гри треку
def play_music():
    current_item = player.main_app.MUSIC_LISTBOX.curselection()
    if current_item:
        if not state.is_playing: # перевіряємо чи не грає зараз трек щоб почати його гру
            current_item = current_item[0]
            music_path = get_full_path(f"resources/music/{added_music[current_item]}")
            
            player.main_app.CURRENT_MUSIC_LEN = handle_music_len(pygame.mixer.Sound(music_path).get_length())
            player.main_app.CURRENT_SONG_NAME = handle_music_name(added_music[current_item])
        
        if not state.is_playing and not state.is_paused:
            place_music_name()
        
        if not state.is_loaded: # умова загрузки треку
            pygame.mixer.music.load(music_path)
            music_len = int(pygame.mixer.Sound(music_path).get_length())
            
            current_music_time()
            
            len_in_mins = music_len // 60
            len_in_seconds = music_len - (len_in_mins * 60)

            place_music_len(len_in_seconds, len_in_mins)

            pygame.mixer.music.play()
            state.on_load()
            
        if state.is_paused and state.is_loaded: # умова паузи треку
            pygame.mixer.music.unpause()
            state.on_unpause()