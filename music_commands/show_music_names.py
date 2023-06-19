from music_commands.get_music_names import get_music_names

added_music = []

def handle_music_name(music_name):
    music_name = music_name.split(".mp3")[0]
    if len(music_name) > 28:
        music_name = music_name[:23]
    return music_name

def show_music_names(listbox):
    for music_name in get_music_names():
        if music_name not in added_music:
            added_music.append(music_name)
            listbox.insert("end", handle_music_name(music_name))

def show_mixed_music_names(listbox):
    listbox.delete(0, "end")
    for music_name in added_music:
        listbox.insert("end", handle_music_name(music_name))