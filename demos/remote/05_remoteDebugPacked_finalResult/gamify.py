from ui import show_message

# we need to change the way we import the external game module to ensure
# the `guess_game.py` file is imported from outside the packed executable
# from games.guess_game import play_game
import os
import sys
import importlib

try:
    start_file = __file__  # unpacked
except NameError:  # __file__ not defined
    start_file = sys.executable  # packed into .exe
app_dir = os.path.dirname(start_file)
sys.path.insert(0, app_dir)
play_game = importlib.import_module('games.guess_game').play_game


if __name__ == '__main__':
    show_message('¡Hola! ¡Vamos a jugar!')
    play_game()
    show_message('¡Gracias por jugar, nos vemos!')
