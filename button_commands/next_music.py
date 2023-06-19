import player # імпортуємо модуль player
from gui_commands import place_music_name, skip_music, current_music_time # імпортуємо функцію place_music_name та skip_music із папки gui_commands
from music_commands import handle_music_name # імпортуємо функцію handle_music_name з папки music_commands

from music_commands.show_music_names import added_music # імпортуємо список added_music (у який записується додана музика) з моудлю show_music_names з папки music_commands
import pygame # імпортуємо бібліотеку pygame
from paths.path_utils import get_full_path # функцію get_full_path (для знаходження повного шляху) з модулю path_utils з папки paths

# ініціалізація
pygame.init() # ініціалізуємо pygame
pygame.mixer.init() # ініціалізуємо mixer у pygame

# функція відповідальна за перехід до наступного треку
def next_music():
    current_item = list(player.main_app.MUSIC_LISTBOX.curselection())
    
    # умова за якою відбувається переміщення до наступного треку
    try:
        if not current_item and len(added_music) >= 1: 
            player.main_app.MUSIC_LISTBOX.select_set(0) #
            player.main_app.MUSIC_LISTBOX.activate(0) # використовуємо activate (для вбирання нижніх підкреслення)   
            skip_music(0)
            
        else:
            player.main_app.MUSIC_LISTBOX.select_clear(current_item[0], current_item[0])
            
            if current_item[0] + 1 > len(added_music) - 1:
                player.main_app.MUSIC_LISTBOX.select_set(0)
                player.main_app.MUSIC_LISTBOX.activate(0) # використовуємо activate (для вбирання нижніх підкреслення)
                skip_music(0)
                
            else: 
                player.main_app.MUSIC_LISTBOX.select_set(current_item[0] + 1)
                player.main_app.MUSIC_LISTBOX.activate(current_item[0] + 1) # використовуємо activate (для вбирання нижніх підкреслення)
                skip_music(current_item[0] + 1)
    except IndexError:
        pass