import os
import time 

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
