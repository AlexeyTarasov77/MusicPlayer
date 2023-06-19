from customtkinter import CTkButton
from gui_config import *

def create_buttons(master, width, image = None, height = None, command = None): # функція створення кнопок
    return CTkButton(
        master = master,
        width = width,
        height = forall_button_height if not height else height,
        corner_radius = forall_corner_radius,
        border_width = forall_border_width,
        border_color = forall_border_color,
        fg_color = forall_fg_color,
        hover_color = btn_hover_color,
        image = image,
        text = '',
        command = command if command else None
    )
