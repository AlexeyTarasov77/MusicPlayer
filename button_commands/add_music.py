from music_commands import get_music_file_path
from music_commands import show_music_names
from extra_commands import *
import player


def add_music(): # функція додавання нових треків
    music_path = get_music_file_path()
    try:
        copy_file(music_path)
        show_music_names(listbox = player.main_app.MUSIC_LISTBOX)
    except shutil.SameFileError:
        pass
    #show_music_names(
#
    #)
   
    # music_path = c_get_music.get_music_file_path()
    # c_file.copy_file(music_path)
    # c_get_file_names.music_names = c_get_file_names.get_file_names()
    
   