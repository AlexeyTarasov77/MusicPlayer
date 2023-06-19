import player
from music_commands.get_music_file_path import *
from music_commands.show_music_names import *
from extra_commands import *
import os
from paths.path_utils import get_full_path
import pygame

pygame.init()
pygame.mixer.init()

def delete_music(): # функція видалення треків
    try:
        current_item = player.main_app.MUSIC_LISTBOX.curselection()[0]
    
        music_path = get_full_path(f"resources/music/{added_music[current_item]}")
    
        os.remove(music_path)

        player.main_app.MUSIC_LISTBOX.delete(current_item, current_item)
        del added_music[current_item]
        show_music_names(listbox = player.main_app.MUSIC_LISTBOX)

    except IndexError:
        pass
    except PermissionError:
        pass