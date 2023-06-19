import pygame # імпортуємо pygame
from status import * # імпортуємо модуль status

# ініціалізація
pygame.init() # ініціалізацуємо pygame
pygame.mixer.init() # ініціалізацуємо mixer у pygame

# функція відповідальна за паузу треку
def pause_music():
    if state.is_playing: # перевіряємо чи грає музика для її паузи
        pygame.mixer.music.pause() 
        state.on_pause()