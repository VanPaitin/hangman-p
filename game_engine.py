from sys import exit
from termcolor import colored
from inflect import engine
from messages import Message
from utilities import get_valid_choice, get_validated_input, VALID


inflector = engine()

class GameEngine:
    def __init__(self, *, chances, game_word, player, can_save=False):
        self._chances = chances
        self._game_word = game_word.lower()
        self._player = player
        self._can_save = can_save

        self.initialize_game_data()


    def initialize_game_data(self):
        self._misses = set()
        self._right_guesses = set()
        self._guess_prompt = colored('Enter a guess: ', 'yellow')

    @property
    def player(self):
        return self._player

    @property
    def word_control(self):
        initial_string = '_' * len(self._game_word)
        string_list = list(initial_string)
        for letter in self._right_guesses:
            for i, ch in enumerate(self._game_word):
                if ch == letter:
                    string_list[i] = letter

        return ''.join(string_list)


    @property
    def ui_word_control(self):
        return colored(self.word_control.replace('_', ' __ ').upper().rstrip(), 'cyan', attrs=['bold', 'italic'])


    @property
    def is_game_won(self):
        return len(self._right_guesses) == len(set(self._game_word))


    @property
    def attempts(self):
        return len(self._right_guesses) + len(self._misses)


    @property
    def history(self):
        parts = []

        for guess_type, guesses in [('miss', self._misses), ('right guess', self._right_guesses)]:
            options = f': ({inflector.join(list(guesses))})' if guesses else ''
            parts.append(f'{inflector.no(guess_type, len(guesses))}{options}')

        return 'You have ' + ' and '.join(parts)


    def run(self):
        print(self.ui_word_control)

        while self.attempts < self._chances:
            guess = get_validated_input(self.guess_validator)(self._guess_prompt)
            self._compare_guess(guess.lower())
            print(self.ui_word_control)
            if self.is_game_won:
                return self.win_game()

            remaining = self._chances - self.attempts
            print(f'You have {remaining} {inflector.plural("chance", remaining)} left')

        self.lose_game()


    def guess_validator(self, guess):
        guess = guess.lower()
        match guess:
            case ':c':
                print(self._game_word)

                return (False, self._guess_prompt)
            case ':h' | 'history':
                print(self.history)

                return (False, self._guess_prompt)
            case 'quit' | ':q':
                if self._can_save:
                    GamePersistence.save_game(self)

                exit(colored('Goodbye', 'yellow'))
        if len(guess) != 1: return (False, 'Enter just one character please: ')

        if guess in self._right_guesses | self._misses:
            return (False, f'You have used {guess} already, try again ')

        return VALID


    def _compare_guess(self, guess):
      if guess.lower() in self._game_word:
          print(colored('Nice one!', 'green'))
          self._right_guesses.add(guess)
      else:
          print(Message.bad_guess())
          self._misses.add(guess)


    def __str__(self):
        return f"{self._player}  ===>>>     {self.ui_word_control}\n"\
  		f"\t{self._chances - self.attempts} chances left and you have used {inflector.join(list(self._misses))}"


    def win_game(self):
        print(colored(f'Congratulations {self._player}! You have won the game', 'cyan', attrs=['bold', 'italic']))

        self.end_game()



    def lose_game(self):
        print(colored(f'Game over! You lose! Sorry {self._player}', 'red', attrs=['bold']))
        print('The word is', colored(f'{self._game_word.upper()}', 'yellow', attrs=['bold', 'italic']))

        self.end_game()


    def end_game(self):
        GamePersistence.delete_game(self)

        if get_valid_choice(
            ['r', 'restart', 'q', 'quit'],
            Message.end_games()
        ).lower() in ['q', 'quit']: exit('Goodbye!')


from game_persistence import GamePersistence

