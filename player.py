import customtkinter as ctk # іпортуємо бібліотеку customtkinter та зкорочуємо її ім'я на ctk
from gui_config import * # імпортуємо все із папки gui_config
from gui_commands import * # імпортуємо все із папки gui_commands

from button_commands import * # імпортуємо все із папки button_commands
import images # імпортуємо модуль images (у ньому створюються картинки для кнопок)
from tkinter import Listbox, PhotoImage # іпортуємо Listbox (для створення лістбоксу у якому буе список треків)

from music_commands import * # імпортуємо все із папки music_commands
from paths import app_icon_win_path, app_icon_linux_path # імпортуємо змінну app_icon_path (у ній зберігається шлях до іконки додатку) з папки paths
from images import volume_icon_image # імпортуємо об'єкт картинки volume_icon_image (картинки яка символізує мішкер гучності треку) з файлу images (у якому створюються об'єкти картинок)

class App(ctk.CTk): # основний класс додатку у якому проходять всі процеси що є у самому додатку
    def __init__(self, app_width, app_height):
        super().__init__()
        self.configure_app(app_width, app_height)
             
        # Налаштування гучностi
        self.VOLUME = 1.0 # змінна з початковим значенням гучності

        self.create_fonts()
        
        self.create_stringvars()
        
        self.create_frames() # створюємо фрейми
        self.place_frames() # розміщуємо фрейми
        
        self.create_labels()
        self.place_labels()
        
        self.create_buttons() # визиваємо метод створення кнопок
        self.place_buttons() # визиваємо метод розміщення кнопок

        self.create_other_elements()
        self.place_other_elements()

        show_music_names(listbox = self.MUSIC_LISTBOX) # відображаємо ім'я треків при входу до програми у лістбоксі для них
    


    def configure_app(self, app_width, app_height):
        self.configure(fg_color = app_fg_color) # задаємо колір фону додатку
        self.resizable(False, False) # робимо розміри екрану не змінними
        self.title("Music Player") # задаємо ім'я додатку
        self.center_app(app_width, app_height)
        self.set_icon()
        
    
    def set_icon(self):
        if os.name == 'nt':
            self.iconbitmap(app_icon_win_path)
        elif os.name == 'posix':
            self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file = app_icon_linux_path))
        
            
    
    def center_app(self, app_width, app_height):
        # розміри екрану
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # задаємо координату розміщення вікна по середині
        center_x = screen_width // 2 - app_width // 2 
        center_y = screen_height // 2 - app_height // 2
        
        self.geometry(f'{app_width}x{app_height}+{center_x}+{center_y}')
    
    
    
    def create_fonts(self):
        # font_path = 'resources/font.ttf' # шлях до файлу шрифта
        # pyglet.font.add_file(font_path)

        self.LISTBOX_FONT = ctk.CTkFont( # створюємо шрифт
            family = 'JetBrains Mono',
            size = 11
        )

        self.MUSIC_NAME_FONT = ctk.CTkFont( # створюємо шрифт
            family = 'JetBrains Mono',
            size = 13
        )

        self.VOLUME_LABEL_FONT = ctk.CTkFont( # створюємо шрифт
            family = 'JetBrains Mono',
            size = 23
        )
        
    
    def create_stringvars(self):
        self.VOLUME_STRINGVAR = ctk.StringVar(value = "Volume: 50%") # властивість у яку записуються проценти гучності гри треку у даний момент
        self.CURRENT_SONG_NAME_STRING = ctk.StringVar(value = "No song playing now") # властивість у якій міститься назва треку який зараз грає
        self.TIME_LABEL_STRINGVAR = ctk.StringVar(value = "00:00 - 00:00") # властивість у яку записується час гри треку та скільки всього він має грати        


    # створювання фреймів
    def create_frames(self):
        self.RIGHT_SIDE_FRAME = create_frame( # фрейм у якому розміщується кнопки з правої сторони
                master = self,
                width = right_side_frame_width,
                height = right_side_frame_height
        )
        self.BOTTOM_SIDE_FRAME = create_frame( # фрейм у якому розміщується кнопки з нижньої сторони
                master = self,
                width = bottom_side_frame_width,
                height = bottom_side_frame_height
        )
        self.MUSIC_NAME_FRAME = create_frame( # фрейм у якому розміщується лейбл з ім'ям треку який зараз грає
            master = self,
            width = right_side_frame_width,
            height = 30
        )
        music_listbox_height = 21 if os.name == 'nt' else 18
        self.MUSIC_LISTBOX = Listbox( # створюємо лістбокс у якому зберігаються ім'я треків
            master = self,
            bg = forall_fg_color,
            fg = 'white',
            width = 27,
            height = music_listbox_height,
            font = self.LISTBOX_FONT,
            highlightbackground = "black",
            selectbackground = btn_hover_color,
            highlightcolor = 'black'
        )
    
    # метод відповідальний за розміщення фреймів
    def place_frames(self):
        self.RIGHT_SIDE_FRAME.place(x = 20, y = 40)
        self.BOTTOM_SIDE_FRAME.place(x = 40, y = 373)
        self.MUSIC_NAME_FRAME.place(x = 230, y = 30)
        self.MUSIC_LISTBOX.place(x = 223, y = 65) # розміщуємо лист бокс з ім'ями треків


    def create_labels(self):
        self.TIME_LABEL = ctk.CTkLabel(
            master = self,
            width = 50,
            height = 15,
            textvariable = self.TIME_LABEL_STRINGVAR,
            font = self.MUSIC_NAME_FONT
        )
        self.VOLUME_LABEL = ctk.CTkLabel( # створюємо лейбл у який будуть виводиться проценти гучності гри треку у даний момент
            master = self,
            width = 15,
            height = 15,
            textvariable = self.VOLUME_STRINGVAR,
            text_color = forall_fg_color,
            font = self.VOLUME_LABEL_FONT
        )
        self.MUSIC_NAME_LABEL = ctk.CTkLabel( # створюємо лейбл у якому розміщується назва треку який зараз грає
            master = self.MUSIC_NAME_FRAME,
            width = 15,
            height = 15,
            text_color = "white",
            textvariable = self.CURRENT_SONG_NAME_STRING,
            font = self.MUSIC_NAME_FONT   
        )
        self.VOLUME_ICON_LABEL = ctk.CTkLabel( # стврюємо лейбл у якому міститься картинка яка символізує мішкер гучності треку
            master = self,
            text = '',
            image = volume_icon_image
        )


    def place_labels(self):
        self.TIME_LABEL.place(x = 55, y = 15)
        self.VOLUME_LABEL.place(x = 20, y = 445) # розміщуємо лейбл у який будуть виводиться проценти гучності гри треку у даний момент
        self.MUSIC_NAME_LABEL.place(relx = 0.5, rely = 0.5, anchor = 'center') # розміщуємо лейбл с текстом того треку який зараз грає (у данному випалку просто текст) "No song playing now"
        self.VOLUME_ICON_LABEL.place(x = 198, y = 445) # розміщуємо лейбл у якому міститься картинка яка символізує мішкер гучності треку


    # метод відповідальний за створення кнопок
    def create_buttons(self):
        # Перший ряд
        self.PLAY_BUTTON = create_buttons( # кнопка початку гри треку
                master = self.RIGHT_SIDE_FRAME, 
                width = big_button_width,
                image = images.play_btn,
                command = play_music  
        )   
        # Другий ряд
        self.NEXT_BUTTON = create_buttons( # кнопка переходу до наступного треку
                master = self.RIGHT_SIDE_FRAME, 
                width = small_button_width,
                image = images.next_btn,
                command = next_music
        )
        self.PREVIOUS_BUTTON = create_buttons( # кнопка перехіду до минулого треку
                master = self.RIGHT_SIDE_FRAME, 
                width = small_button_width,
                image = images.prev_btn, 
                command = prev_music
        )
        
        # Третій ряд
        self.PAUSE_BUTTON = create_buttons( # кнопка паузи треку
                master = self.RIGHT_SIDE_FRAME, 
                width = big_button_width,
                image = images.pause_btn,
                command = pause_music

        )
        
        # Четвертий ряд
        self.STOP_BUTTON = create_buttons( # кнопка стопу треку
                master = self.RIGHT_SIDE_FRAME, 
                width = big_button_width,
                image = images.stop_btn,
                command = stop_music   
        )
        
        # П'ятий ряд
        self.ADD_BUTTON = create_buttons( # кнопка додавання треків
                master = self.BOTTOM_SIDE_FRAME, 
                width = small_button_width,
                image = images.add_btn,
                command = add_music
        )
        self.DELETE_BUTTON = create_buttons( # кнопка видалення треків
                master = self.BOTTOM_SIDE_FRAME, 
                width = small_button_width,
                image = images.delete_btn,
                command = delete_music      
        )
        self.MIX_BUTTON = create_buttons( # кнопка мміксування треків
                master = self,
                width = 200,
                height = 40,
                image = images.mix_btn,
                command = mix_music           
        )
    
    # метод відповідальний за розміщення кнопок
    def place_buttons(self):
        # Перший ряд
        self.PLAY_BUTTON.grid(row = 0, column = 0)
        
        # Другий ряд
        self.NEXT_BUTTON.grid(row = 1, column = 0, sticky= ctk.E, pady= v_margin)
        self.PREVIOUS_BUTTON.grid(row = 1, column = 0, sticky= ctk.W)
        
        # Третій ряд
        self.PAUSE_BUTTON.grid(row = 2, column = 0)
        
        # Четвертий ряд
        self.STOP_BUTTON.grid(row = 3, column = 0, pady = v_margin)

        # П'ятий ряд
        self.ADD_BUTTON.grid(row = 0, column = 0)
        self.DELETE_BUTTON.grid(row = 0, column = 1, padx = h_margin)
        self.MIX_BUTTON.place(x = 220, y = 393)


    def create_other_elements(self):
        self.VOLUME_SLIDER = ctk.CTkSlider( # створюємо слайдер (мішкер) для змінювання гучності гри треку 
            master = self,
            width = 200,
            from_ = 0, 
            to = 1,
            number_of_steps = 100,
            progress_color = forall_fg_color,
            button_color = forall_fg_color,
            button_hover_color = btn_hover_color,
            command = on_slider_change
        )
    
    def place_other_elements(self):
        self.VOLUME_SLIDER.place(x = 220, y = 450)  # розміщуємо слайдер (мішкер) для змінювання гучності гри треку


# вікно додатку
main_app = App(440, 490)