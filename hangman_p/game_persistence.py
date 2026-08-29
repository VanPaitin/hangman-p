import pickle
from pathlib import Path
from sys import exit as sys_exit

from cli_input_validator import get_valid_choice
from termcolor import colored

from .messages import Message


class GamePersistence:
    save_dir = Path.home() / ".hangman-p"
    saved_games = save_dir / "saved_games.pkl"

    @classmethod
    def load_all(cls):
        try:
            with cls.saved_games.open("rb") as games_file:
                return pickle.load(games_file)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return []

    @classmethod
    def _save_all(cls):
        cls.save_dir.mkdir(exist_ok=True)
        with cls.saved_games.open("wb") as games_file:
            pickle.dump(cls.engines, games_file)

    @classmethod
    def save_game(cls, engine):
        option = get_valid_choice(
            ["Yes", "No"], "Do you want to save your game? type 'Yes' or 'No': "
        )

        if option.lower() == "yes":
            if engine not in cls.engines:
                cls.engines.append(engine)

            cls._save_all()
            print(colored("Goodbye, your game has been saved successfully", "green"))
            sys_exit(0)

    @classmethod
    def load_game(cls):
        cls.player = input("Enter the name you used to play the game: ").lower()
        cls.player_games = [
            game for game in cls.engines if game.player.lower() == cls.player
        ]

        if not cls.player_games:
            raise ValueError(Message.no_saved_game())

        cls.display_games()

        choice = get_valid_choice(
            [str(i + 1) for i in range(len(cls.player_games))],
            prompt="Now enter the number for the game you want to play: ",
        )

        print(colored("\nNow continue playing...", "green", attrs=["bold"]))

        return cls.player_games[int(choice) - 1]

    @classmethod
    def display_games(cls):
        message = f"\nHere are the saved games found for {cls.player.capitalize()}\n\n"

        for i, game in enumerate(cls.player_games):
            message += f"{i + 1}.\t{game}\n"

        print(message)

    @classmethod
    def delete_game(cls, engine):
        if engine in cls.engines:
            cls.engines.remove(engine)
            cls._save_all()


GamePersistence.engines = GamePersistence.load_all()
