import pygame
from status import *
import player
from gui_commands import place_music_name

pygame.init()
pygame.mixer.init()

def stop_music(): # функція відповідальная за стоп музики
    player.main_app.TIME_LABEL_STRINGVAR.set('00:00 - 00:00')
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    player.main_app.CURRENT_SONG_NAME = "No song playing now"
    place_music_name()
    state.on_stop()