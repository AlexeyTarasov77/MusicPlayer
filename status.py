

class BtnState: #
    def __init__(self):      
        self.is_paused = False
        self.is_loaded = False
        self.is_playing = False
    
    def on_play(self): # метод змінення значень властивостей при натисканні на кнопку play
        self.is_paused = False
        self.is_loaded = True
        self.is_playing = True

    def on_stop(self): # метод змінення значень властивостей при натисканні на кнопку stop
        self.is_paused = False
        self.is_loaded = False
        self.is_playing = False

    def on_pause(self): # метод змінення значень властивостей при натисканні на кнопку pause
        self.is_paused = True
        self.is_loaded = True
        self.is_playing = False

    def on_unpause(self): #
        self.is_paused = False
        self.is_loaded = True
        self.is_playing = True
        
    def on_load(self): #
        self.is_paused = False
        self.is_loaded = True
        self.is_playing = True

# створюємо об'єкт класу BtnState
state = BtnState()