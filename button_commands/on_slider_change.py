import pygame # імпортуємо бібліотеку pygame
import player # імпортуємо модуль player

pygame.mixer.init() # ініціалізуємо mixer у бібліотеці pygame

# функція відповідальна за працю слайдеру (мішкеру) для змінювання гучності гри треку
def on_slider_change(value):
    pygame.mixer.music.set_volume(float(value)) # задаємо функціонал змінювання гучності трека за допомогою слайдеру (мішкеру)
    player.main_app.VOLUME_STRINGVAR.set("Volume: " + str(int(float(value) * 100)) + "%") # створюємо формулу для записування звичайних процентів у лейбл з процентами гучності треку який зараз грає
