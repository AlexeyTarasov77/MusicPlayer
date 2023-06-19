import customtkinter as ctk

def create_label(master, width, height, text_color, text): # функція створення лейблів
    return ctk.CTkLabel(
        master = master,
        width = width, 
        height = height, 
        bg_color ='transparent',
        text_color = text_color,
        text = text
    )
