from importlib.resources import files
from random import choice

from cli_input_validator import VALID, get_validated_input
from maskpass import askpass
from termcolor import colored

from .game_engine import GameEngine

class Level:
    config = {
        "1": {"min": 4, "max": 8, "chances": 9},
        "2": {"min": 9, "max": 13, "chances": 12},
        "3": {"min": 14, "max": 25, "chances": 17},
    }

    def __init__(self, difficulty, player, challenger=None):
        self.difficulty = difficulty
        self.player = player
        self.challenger = challenger
        info = (
            f"\n        Welcome {player}, In this level, you will have "
            f"{self.chances} chances to guess the word correctly\n        "
        )
        print(colored(info, "yellow"))
        self.game_word = self.challenge_word() if challenger else self.generate_word()

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        if difficulty not in ["1", "2", "3"]:
            raise ValueError("Invalid Value")

        self._difficulty = difficulty
        level_config = self.config[difficulty]
        self.min = level_config["min"]
        self.max = level_config["max"]
        self.chances = level_config["chances"]

    def generate_word(self):
        dictionary_path = files("hangman_p").joinpath("dictionary.txt")
        with dictionary_path.open() as dictionary:
            return choice([line.rstrip() for line in dictionary if self.is_valid_length(line)])

    def challenge_word(self):
        def word_validator(word):
            error = (
                f"Word length not correct! Make it between {self.min} & "
                f"{self.max} characters\n"
            )
            return VALID if self.is_valid_length(word) else (False, error)

        prompt = (
            f"Now, enter your challenge word {self.challenger}, it will be hidden: "
        )
        return get_validated_input(word_validator, input_function=askpass)(prompt)

    def is_valid_length(self, line):
        return self.min <= len(line) <= self.max

    def run_engine(self):
        engine = GameEngine(
            chances=self.chances,
            game_word=self.game_word,
            player=self.player,
            can_save=not self.challenger,
        )

        engine.run()
