# $ pip install debugpy

import os
import debugpy

if not debugpy.is_client_connected():
    this_dir = os.path.dirname(__file__)
    debugpy.log_to(os.path.join(this_dir, 'debug_logs'))  # optional
    debugpy.listen(5678)
    print('Esperando por el cliente de depuración...')
    debugpy.wait_for_client()  # optional

# original script
import random
from ui import show_message, ask_for_input
from audioplayer import play_wav

# game settings
MIN_NUMBER, MAX_NUMBER = 1, 20
MAX_TRIES = 4

def play_game() -> None:
    """Play game: Guess the Number

    1. Generate a random secret number between MIN_NUMBER and MAX_NUMBER
    2. Main loop:
        -     Ask for a number and compare it with the secret number
        - If the numbers match, execute the "winner" block and exit
        - Otherwise, execute the "lower" or "higher" block and continue to next try
    3. If MAX_TRIES is reached, execute the "looser" block and exit
    """
    
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)  # generate a random number
    
    # message to show before each bet prompt
    bet_prefix = f"El número secreto está entre {MIN_NUMBER} y {MAX_NUMBER}\n"  # hint for first try only
    for current_bet in range(1, MAX_TRIES +1):
        last_bet = int(ask_for_input(f"{bet_prefix}Tu apuesta: "))
        if last_bet == secret_number:  # succeed -> winner
            play_wav('winner')
            show_message(f"¡Buen trabajo! ¡Lo has resuelto en {current_bet} intentos!")
            return
        elif last_bet < secret_number:  # bet is too low
            play_wav('low')
            bet_prefix = "Tu apuesta es muy baja."
        elif last_bet > secret_number:  # bet is too high
            play_wav('high')
            bet_prefix = "Tu apuesta es muy alta."
    
    # max tries exhausted: game over -> looser
    play_wav('looser')
    show_message(f"¡Oooh, nooo, has perdido! El número secreto era {secret_number}")


if __name__ == '__main__':
    show_message('¡Hola! ¡Vamos a jugar!')
    play_game()
    show_message('¡Gracias por jugar, nos vemos!')
