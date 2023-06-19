import player 
import pygame
from status import *

pygame.mixer.init()
# if f'{current_min:02d}:{current_sec % 60:02d} == player.main_app.CURRENT_MUSIC_LEN:
def current_music_time():
    current_sec = pygame.mixer.music.get_pos() // 1000
    current_min = current_sec // 60
    
    if player.main_app.CURRENT_SONG_NAME != "No song playing now":
        player.main_app.after(100, current_music_time)
        player.main_app.TIME_LABEL_STRINGVAR.set(f'{current_min:02d}:{current_sec % 60:02d} - {player.main_app.CURRENT_MUSIC_LEN}')
    
    
    if f'{current_min:02d}:{current_sec % 60:02d}' == player.main_app.CURRENT_MUSIC_LEN:
        player.main_app.CURRENT_SONG_NAME = "No song playing now"
        player.main_app.CURRENT_SONG_NAME_STRING.set("No song playing now")
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        state.on_stop()
        player.main_app.TIME_LABEL_STRINGVAR.set(f'00:00 - 00:00')