from PIL import Image
from customtkinter import CTkImage

def create_image(image_path, size): # функція створення картинок
    return CTkImage(
        dark_image = Image.open(image_path),
        size = size
    )