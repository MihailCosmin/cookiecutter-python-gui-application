import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import random
from pathlib import Path

def read_in_words():
    file_path = Path(__file__).parent / "english_words.txt"  
    lines = [] 
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())  # add each line to the list, stripped of any whitespace
    return lines

class Hangman(toga.App):
    valid_alphabet = set("abcdefghijklmnopqrstuvwxyz")
    all_words = read_in_words()
    
    #styles
    game_font = "Century Schoolbook"
    title_style = Pack(padding=(0, 5), font_family=game_font, font_size=20, text_align="center", font_weight="bold")
    button_style = Pack(padding=(0, 5), font_family=game_font, font_size=15, text_align="center")
    game_over_style = Pack(padding=(0, 5), font_family=game_font, font_size=50, text_align="center", font_weight="bold")
    secret_word_style = Pack(padding=(0, 5), font_family=game_font, font_size=35, text_align="center", font_weight="bold")
    
    def startup(self):
        self.secret_word = ""
    
        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(toga.Label("Welcome to Hangman!", style=Hangman.title_style ))
        main_box.add(toga.Button("Play Hangman" , style=Hangman.button_style, on_press=self.start_new_game))
        main_box.add(toga.Button("Start Game with Own Word", style=Hangman.button_style, on_press=self.enter_own_word))

        self.main_window = toga.MainWindow(title="Hangman", position=(100, 100), size=(800, 600))
        self.main_window.content = main_box
        self.main_window.show()
        
    def enter_own_word(self, widget):
        box = toga.Box(style=Pack(direction=COLUMN))
        box.add(toga.Label("Enter your secret word:", style=Hangman.title_style ))
        box.add(toga.TextInput(placeholder="Enter Your Word Here", on_change=self.update_secret_word_handler)) #could add valitors here if needed
        box.add(toga.Button("Start Game", style=Hangman.button_style, on_press=self.start_new_game))
        self.main_window.content = box
        self.main_window.show()
        
    def start_new_game(self, widget):

        if widget.text == "Play Hangman" or widget.text == "Start a New Game":
            self.secret_word = self.get_word() # get a random word
            print(self.secret_word)
        
        #initialize variables used for each game
        self.letters = set(self.secret_word)
        self.used_letters = []
        self.lives = 7
        self.correct_letters = set()
        self.hangman_image_path = str(Path(__file__).parent / "hangman_images" )
        self.hangman_image = "/hangman-0" #set to beginning
        self.revealed_word = ["_"] * len(self.secret_word)
        self.game_state()
        
    def get_word(self):
        random_item = random.choice(Hangman.all_words)
        return random_item
        
    def game_state(self): 
        box = toga.Box(style=Pack(direction=COLUMN))
        
        #heading
        box.add(toga.Label("Guess a Letter!", style=Hangman.title_style ))
        box.add(toga.Label("Word: " + " ".join(self.revealed_word), style=Hangman.secret_word_style))
        box.add(toga.TextInput(validators=[self.max_length, self.letters_only], on_change=self.process_letter))
        
        # used letters + lives
        box.add(toga.Label("Used Letters: " + " ".join(self.used_letters), style=Hangman.title_style))
        box.add(toga.Label("Lives: " + str(self.lives), style=Hangman.title_style))
        
        #buttons
        box.add(toga.Button("Start a New Game", style=Hangman.button_style, on_press=self.start_new_game))
        box.add(toga.Button("Play Hangman with Own Word", style=Hangman.button_style, on_press=self.enter_own_word))
        
        #image
        box.add(toga.ImageView(image=self.hangman_image_path + self.hangman_image + ".PNG"))
        
        self.main_window.content = box
        
    def kill_game(self, widget):
        self.end_game(victory=False)
        
    def process_letter(self, widget):
        self.used_letters.append(widget.value)
        if widget.value in self.letters: #if letter is in word, replace underscore with letter
            self.correct_letters = self.correct_letters.union(widget.value)
            
            for i in range(len(self.secret_word)): 
                if self.secret_word[i] in self.correct_letters:
                    self.revealed_word[i] = self.secret_word[i]
            
        else: #else, remove lives & change image
            self.lives = self.lives - 1
            number = int(self.hangman_image[-1]) + 1
            self.hangman_image = self.hangman_image[:-1] + str(number)
        
        if self.lives == 0: #check if game is over
            self.end_game(victory=False)
        elif "_" not in self.revealed_word:
            self.end_game(victory=True)
        else:
            self.game_state()
            
    def end_game(self, victory=False):
        box = toga.Box(style=Pack(direction=COLUMN))
        
        if victory:
            box.add(toga.Label("You won! :)", style=Hangman.game_over_style))
            img_path = self.hangman_image_path + "/victory.PNG"
        else:
            box.add(toga.Label("You lost! :C", style=Hangman.game_over_style))
            img_path = self.hangman_image_path + "/death.PNG"
            
        box.add(toga.Label("The word was: " + self.secret_word, style=Hangman.secret_word_style))
        box.add(toga.Button("Start a New Game", style=Hangman.button_style, on_press=self.start_new_game))
        box.add(toga.Button("Play Hangman with Own Word", style=Hangman.button_style, on_press=self.enter_own_word))
        
        box.add(toga.ImageView(image=img_path))
        self.main_window.content = box
        self.main_window.show()


    
    #save variable handler
    def update_secret_word_handler(self, widget):
        self.secret_word = widget.value
    
    # validators
    def letters_only(self, letter):
        lowercase = letter.lower()
        if lowercase in Hangman.valid_alphabet:
            return None
        else:
            return "Please enter a letter"
        
    def max_length(self, letter):
        if len(letter) > 1:
            return "Please enter only one letter"
        else:
            return None

def main():
    return Hangman()
    
