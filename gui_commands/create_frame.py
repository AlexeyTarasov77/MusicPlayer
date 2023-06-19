from customtkinter import CTkFrame
from gui_config import *

def create_frame(master, width, height): # функція створення фреймів
    return CTkFrame(
        master = master,
        width = width,
        height = height,
        fg_color = app_fg_color,
        bg_color = 'transparent',
        corner_radius = forall_corner_radius,
        border_width = forall_border_width,
        border_color = app_fg_color
    )