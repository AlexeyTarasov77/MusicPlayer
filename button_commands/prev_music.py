import player # імпортуємо модуль player
from music_commands.show_music_names import added_music # імпортуємо список added_music (у який записується додана музика) з моудлю show_music_names з папки music_commands
import pygame # імпортуємо бібліотеку pygame

from gui_commands import place_music_name, skip_music, current_music_time # імпортуємо функцію place_music_name та skip_music із папки gui_commands
from music_commands import handle_music_name # імпортуємо функцію handle_music_name з папки music_commands
from paths import get_full_path # функцію get_full_path (для знаходження повного шляху) з папки paths

# ініціалізація
pygame.mixer.init()

# функція відповідальна за переміщення до минулого треку
def prev_music():
    current_item = list(player.main_app.MUSIC_LISTBOX.curselection())
    #player.main_app.MUSIC_LISTBOX.select_set(3)

    # умова за якою відбувається переміщення до минулого треку
    try:
        if not current_item and len(added_music) >= 1:
            player.main_app.MUSIC_LISTBOX.select_set(len(added_music) - 1)
            player.main_app.MUSIC_LISTBOX.activate(len(added_music) - 1) # використовуємо activate (для вбирання нижніх підкреслення)   
            skip_music(-1)
        
        else:
            player.main_app.MUSIC_LISTBOX.select_clear(current_item[0], current_item[0])

            if current_item[0] == 0:
                player.main_app.MUSIC_LISTBOX.select_set(len(added_music) - 1)
                player.main_app.MUSIC_LISTBOX.activate(len(added_music) - 1) # використовуємо activate (для вбирання нижніх підкреслення)   
                skip_music(-1)
                
            else:    
                player.main_app.MUSIC_LISTBOX.select_set(current_item[0] - 1)
                player.main_app.MUSIC_LISTBOX.activate(current_item[0] - 1) # використовуємо activate (для вбирання нижніх підкреслення)   
                skip_music(current_item[0] - 1)
    except IndexError:
        pass