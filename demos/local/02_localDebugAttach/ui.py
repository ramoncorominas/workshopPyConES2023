def show_message(message: str) -> None:
    """Show a message to the user."""
    
    print(message)

def ask_for_input(question: str) -> str:
    """Ask a question and return the answer."""

    answer = ''
    while answer == '':
        answer = input(question).strip()
    return answer
