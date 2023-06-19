import player
from status import state
import pygame

def place_music_name(): # функція яка розміщує лейбл з ім'ям треку який зараз грає
    if player.main_app.CURRENT_SONG_NAME:
        player.main_app.MUSIC_NAME_LABEL.place(relx = 0.5, rely = 0.5, anchor = 'center')
        player.main_app.CURRENT_SONG_NAME_STRING.set(player.main_app.CURRENT_SONG_NAME)