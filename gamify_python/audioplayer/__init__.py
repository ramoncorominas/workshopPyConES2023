import os
import time 

# we need to monkey patch os.add_dll_directory  for packaging because
# from python >= 3.8 it tries to open library.zip as a directory
def fixed_add_dll_directory(path):
    if '.zip' in path:
        path = path.split('.zip')[0] + '.zip'
    return add_dll_directory_orig(path)


try:  # this will only patch if really needed
    add_dll_directory_orig = os.add_dll_directory
    os.add_dll_directory = fixed_add_dll_directory
finally:
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # hide Pygame's support message
    import pygame as pg 

WAVES_DIR = 'waves'

pg.mixer.init()
pg.init()

def play_wav(sound: str) -> None:
    """Play the corresponding WAV from WAVES_DIR, if it exists."""
    
    sound_file = os.path.join(WAVES_DIR, f"{sound}.wav")
    if os.path.isfile(sound_file):
        pg_sound = pg.mixer.Sound(sound_file)
        pg_sound.play()
        duration = pg_sound.get_length()
        time.sleep(duration)  # Let the sound play 
