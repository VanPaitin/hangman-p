from sys import exit
from messages import Message
from utilities import verify_name_integrity, get_valid_choice
from level import Level
from game_persistence import GamePersistence



def main():
    choice = get_valid_choice(game_actions(), prompt=Message.welcome()).lower()

    while choice in ['i', 'instruction']:
        choice = get_valid_choice(game_actions(), prompt=Message.instruction()).lower()

    match choice:
        case "p" | "play":
            name = verify_name_integrity(Message.game_intro()).capitalize()
            print(f'Hi {name}, ', end='')

            while True:
                play(name)
        case "q" | "quit":
            exit()
        case "l" | "load":
            load()


def game_actions():
    return ['p', 'P', 'play', 'i', 'I', 'instruction', 'q', 'Q', 'quit', 'l', 'L', 'load']


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
        friend_name = verify_name_integrity(f'Please enter the name of your friend: ').capitalize()
        print(f'Hello {name} and {friend_name}, who will like to challenge?')
        challenger = get_challenger(name, friend_name).capitalize()
        player = friend_name if name == challenger else name
        level = Level(difficulty, player, challenger)

    return level



def get_challenger(name, friend_name):
    return get_valid_choice([name, friend_name], f'Please enter one of your names ({name} or {friend_name}): ')


def load():
    try:
        engine = GamePersistence.load_game()
    except ValueError as e: exit(e.args[0])

    engine.run()
    while True:
        play(engine.player)


if __name__ == '__main__': main();
