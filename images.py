from gui_commands import create_image # імпортуємо із папки gui_commands модуль create_image
from paths import * # імпортуємо все із папки paths
from gui_config import * # імпортуємо все із папки gui_config

# Перший ряд
play_btn = create_image( # кнопка початку гри треку
    image_path = play_btn_path,
    size = big_button_size    
)

# Другий ряд
next_btn = create_image( # кнопка переміщення до наступного треку
    image_path = next_btn_path,
    size = small_button_size    
)
prev_btn = create_image( # кнопка переміщення до минулого треку
    image_path = prev_btn_path,
    size = small_button_size    
)

# Третій ряд
pause_btn = create_image( # кнопка паузи треку
    image_path = pause_btn_path,
    size = big_button_size    
)

# Четвертий ряд
stop_btn = create_image( # кнопка стопу треку
    image_path = stop_btn_path,
    size = big_button_size    
)

# П'ятий ряд
add_btn = create_image( # кнопка додання нового треку
    image_path = add_btn_path,
    size = small_button_size    
)

delete_btn = create_image( # кнопка видалення треку
    image_path = delete_btn_path,
    size = small_button_size    
)

mix_btn = create_image( # кнопка міксування треків
    image_path = mix_btn_path,
    size = small_button_size  
)


volume_icon_image = create_image( # іконка для позначення мішкера гучності
    image_path = volume_icon_path,
    size = (20, 20)
)