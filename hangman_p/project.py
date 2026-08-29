from sys import exit as sys_exit

from cli_input_validator import get_valid_choice, get_valid_name

from .messages import Message
from .level import Level
from .game_persistence import GamePersistence

def main():
    choice = get_valid_choice(game_actions(), prompt=Message.welcome()).lower()

    while choice in ['i', 'instruction']:
        choice = get_valid_choice(game_actions(), prompt=Message.instruction()).lower()

    match choice:
        case "p" | "play":
            name = get_valid_name(Message.game_intro()).capitalize()
            print(f'Hi {name}, ', end='')

            while True:
                play(name)
        case "q" | "quit":
            sys_exit()
        case "l" | "load":
            load()


def game_actions():
    return [
        "p",
        "P",
        "play",
        "i",
        "I",
        "instruction",
        "q",
        "Q",
        "quit",
        "l",
        "L",
        "load",
    ]


# This technically begins the game
def play(name):
    level = get_level(name)
    level.run_engine()


def get_level(name):
    option = get_valid_choice(['1', '2'], Message.game_type())
    difficulty = get_valid_choice(['1', '2', '3'], Message.level_choice())

    if option == '2':
        level = Level(difficulty, name)
    else:
        friend_name = get_valid_name("Please enter the name of your friend: ").capitalize()
        print(f'Hello {name} and {friend_name}, who will like to challenge?')
        challenger = get_challenger(name, friend_name).capitalize()
        player = friend_name if name == challenger else name
        level = Level(difficulty, player, challenger)

    return level

def get_challenger(name, friend_name):
    prompt = f"Please enter one of your names ({name} or {friend_name}): "
    return get_valid_choice([name, friend_name], prompt)


def load():
    try:
        engine = GamePersistence.load_game()
    except ValueError as error:
        sys_exit(error.args[0])

    engine.run()
    while True:
        play(engine.player)


if __name__ == "__main__":
    main()
