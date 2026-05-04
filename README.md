# Hangman

#### Video Demo: &nbsp; &nbsp; _[CS50P Final project demo](https://youtu.be/2FduPPZd-YU)_

### Description

**_Hangman_** is a command-line word-guessing game implemented in Python.
Players attempt to guess a hidden word one letter at a time before running out of chances. The game supports multiple difficulty levels, game persistence (saving and loading games), and multiplayer challenge mode.

This project demonstrates concepts such as object-oriented design, input validation, persistence using pickle, modular architecture, and automated testing with pytest.

### Features
* Three difficulty levels with different word lengths
* Multiplayer challenge mode
* Game saving and loading
* Automatic deletion of completed saved games
* Input validation and error handling
* Automated unit tests using pytest
* CLI-based interactive gameplay

### Usage

This game is a REPL game, i.e it is being played from and with the Terminal. To start it just run ```python project.py```

Once started, the game is very intuitive and easy to follow.

###"Welcome to Hangman, the no-nonsense game Be smart, then you live. if not, you'll have to die by Hanging. You have a couple of options to pick from..... Press 'P' or 'play' if you think you are ready for the challenge, You may press 'I' or 'instructions' for a short explanation of how to play You may continue a previously saved game by pressing 'L' or 'load' Or you could just quit by pressing a 'Q' or typing 'quit'" "The word to guess is represented by a row of dashes These dashes represent each letter of the word. Words you cannot use include proper nouns such as names, places, and brands. If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions."

The guessing player must guess all of the letters of the word within a limited amount of chances. Faiure to do so will result in his death by hanging.

#### Important note
In human mode, if the player is typing his word, it will not be displayed on the screen, it will be masked so as not to give the challenged player undue advantage.

#### Extras
>You can actually reveal the word by pressing `:c` or `cheat`. This is a cheat for solving the problem and it is not recommended.

>You can quit at any point by pressing `:q` or typing `quit` whereby you will be asked if you want to save the game or just quit. (The option to save is only available in the computer mode.)
>
>If you press `:h` or type `history`, a list showing your guesses will be displayed.

### Project structure
```bash
project.py                # Main entry point
level.py                  # Difficulty configuration
game_engine.py            # Core gameplay logic
utilities.py              # Helper input validation utilities
dictionary.txt            # list of possible words to be used (Computer mode)
game_persistence.py       # Save/load game handling
requirements.txt          # list of external libraries used
test_project.py           # pytest file
```

### Design Decisions
* **Object-oriented structure:** I wasn't sure whether to use OOP or procedural paradigm. After thinking about what I will like to achieve, I decided that OOP was more convenient as it will handle game states more easily.
* **Pickle-based persistence:** I had the option of shelve or json as well, but I decided to vote for pickle mainly because of its elegant serialization and deserialization of python objects
* **Modular utilities:** This decision was made after I found that I was validating inputs in several places of the program. I decided to extract the logic to `utilities.py` to make input validation reusable and testable.
* **Pytest fixtures:** were used for automated testing of interactive functions by monkeypatching input/output.

### Author
Mayowa Pitan

# Enjoy your Hangman experience and try not to be hanged...
good luck...
