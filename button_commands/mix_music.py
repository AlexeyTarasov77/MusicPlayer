from music_commands.show_music_names import * # імпортуємо все із модулю show_music_names у папці music_commands
import random # імпортуємо модуль random
import player # імпортуємо модуль player

def mix_music(): # функція відповідальна за міксування треків
    random.shuffle(added_music)
    show_mixed_music_names(listbox = player.main_app.MUSIC_LISTBOX)
    if len(added_music) > 1: # умова міксування треків за якою вони здатні міксуватись лише тоді коли є хоч 1 трек
        random_index = random.randint(0, len(added_music) - 1)
        # player.main_app.MUSIC_LISTBOX.select_clear(current_item[0], current_item[0])
        player.main_app.MUSIC_LISTBOX.select_set(random_index)
        player.main_app.MUSIC_LISTBOX.activate(random_index)