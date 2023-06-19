import shutil # іпортуємо бібліотеку shutil (для праці з файлами)
from paths import get_full_path

def copy_file(file_path): # функция копіювання файла мізики у папку з музикою музикального пеєра
    if file_path:
        filename = file_path.split("/")[-1]
        shutil.copy(file_path, get_full_path(f"resources/music/{filename}"))