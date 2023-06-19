import player


def handle_music_len(music_len):
    len_in_mins = int(music_len // 60)
    len_in_seconds = int(music_len - (len_in_mins * 60))
    
    return f'{len_in_mins:02d}:{len_in_seconds:02d}' 

    
    
def place_music_len(len_in_seconds, len_in_mins):
    if len_in_mins < 10:
        player.main_app.TIME_LABEL_STRINGVAR.set(f'00:00 - 0{len_in_mins}:{len_in_seconds}')
    elif len_in_mins >= 10:
        player.main_app.TIME_LABEL_STRINGVAR.set(f'00:00 - {len_in_mins}:{len_in_seconds}')