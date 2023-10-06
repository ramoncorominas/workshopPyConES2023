from audioplayer import play_wav

def show_message(message: str) -> None:
    """Show a message to the user."""
    
    print(message)

def ask_for_input(question: str) -> str:
    """Ask a question and return the answer."""

    answer = ''
    while answer == '':
        play_wav('type')  # typewriter sound
        answer = input(question).strip()
    return answer
