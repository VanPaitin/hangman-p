from termcolor import colored

class Message:
    @staticmethod
    def welcome():
            welcome_message = """\tWelcome to Hangman, the no-nonsense game
        Be smart, then you live. if not, you'll have to die by Hanging.
        You have a couple of options to pick from.....
        Press 'P' or 'play' if you think you are ready for the challenge,
        You may press 'I' or 'instructions' for a short explanation of how to play
        You may continue a previously saved game by pressing 'L' or 'load'
        Or you could just quit by pressing a 'Q' or typing 'quit':
        """

            return colored(welcome_message, "green")


    @staticmethod
    def instruction():
            body = """\tThe word to guess is represented by a row of dashes
        These dashes represent each letter of the word.
        Words you cannot use include proper nouns such as names, places, and brands.
        If the guessing player suggests a letter which occurs in the word,
        the other player writes it in all its correct positions.
        \tThe guessing player wins the game if he gets all letters correctly
        within number of chances afforded. He loses if he exhausts all his chances
        without getting all the letters of the word completely.
        \tNow decide whether you want to 'p'lay or 'q'uit.
        Please do keep in mind that you can press ':h' or 'history' at any time
        during the game to show your guess history or ':q'/'quit' to exit the game
        While quitting the game, you may quit directly or decide to save your
        session to resume at a later time at which point you must press 's':
        """
            return colored(body, "yellow")


    @staticmethod
    def game_intro():
            return colored("Now that you have chosen to play, \nWhat is your name? ", 'green')

    # => Instructs the user to enter a valid name
    @staticmethod
    def verify_name():
        return colored("Please enter a real name, I don't think it is just a space or it contains numbers: ", 'red')


    # => game logic
    @staticmethod
    def game_type():
        return """Select a mode.
        1)\tPlay against a Human Player, press 1
        2)\tPlay against Computer, press 2
        """

    # informs the player of the levels available & their respective difficulties
    @staticmethod
    def level_choice():
        return colored("""    Enter the Level you would like to play. You may press...
        1 for Beginner (4 - 8 character word)
        2 for Intermediate (9 - 12 character word)
        3 for Advanced (word has above 12 characters)
        """, 'yellow')

    @staticmethod
    def end_games():
        return "Press 'r' to restart the game or 'q' to quit: "


    @staticmethod
    def bad_guess():
        return colored("Bad guess, the noose tightens\n", 'red') + 'Try again'


    @staticmethod
    def no_saved_game():
        no_game = colored('You have no saved game with that name.\n', 'red')
        new_game = colored('START A NEW GAME INSTEAD', 'yellow')

        return no_game + new_game
