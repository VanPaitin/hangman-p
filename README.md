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
* Automatic display of numbers, spaces, and punctuation in hidden words
* Automated unit tests using pytest
* CLI-based interactive gameplay

### Installation

To install the game with `uv`:

```bash
uv tool install hangman-p
```

This installs the game in an isolated environment and makes the `hangman-p`
command available globally.

You can also try the game without permanently installing it:

```bash
uvx --from hangman-p hangman-p
```

To install it into your active Python environment with `pip`:

```bash
python -m pip install hangman-p
```

### Usage

Hangman is an interactive terminal game. After installation, start it with:

```bash
hangman-p
```

You can also run it as a Python module:

```bash
python -m hangman_p
```

Once started, the game is very intuitive and easy to follow.

###"Welcome to Hangman, the no-nonsense game Be smart, then you live. if not, you'll have to die by Hanging. You have a couple of options to pick from..... Press 'P' or 'play' if you think you are ready for the challenge, You may press 'I' or 'instructions' for a short explanation of how to play You may continue a previously saved game by pressing 'L' or 'load' Or you could just quit by pressing a 'Q' or typing 'quit'" "The word to guess is represented by a row of dashes These dashes represent each letter of the word. Words you cannot use include proper nouns such as names, places, and brands. If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions."

The guessing player must guess all of the letters of the word within a limited amount of chances. Failure to do so will result in his death by hanging.

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
hangman_p/level.py        # Difficulty configuration
hangman_p/game_engine.py  # Core gameplay logic
hangman_p/dictionary.txt  # list of possible words to be used (Computer mode)
hangman_p/game_persistence.py # Save/load game handling
pyproject.toml            # package metadata and dependencies
test_project.py           # pytest file
```

### Design Decisions
* **Object-oriented structure:** I wasn't sure whether to use OOP or procedural paradigm. After thinking about what I will like to achieve, I decided that OOP was more convenient as it will handle game states more easily.
* **Pickle-based persistence:** I had the option of shelve or json as well, but I decided to vote for pickle mainly because of its elegant serialization and deserialization of python objects
* **Shared input validation:** Interactive input is validated with the reusable [`cli-input-validator`](https://pypi.org/project/cli-input-validator/) package.
* **Pytest fixtures:** were used for automated testing of interactive functions by monkeypatching input/output.

### Contributing

Contributions are welcome. You do not need to build or publish distribution
files to contribute.

1. Fork the repository on GitHub and clone your fork.
2. Create a branch for your change:

```bash
git switch -c feature/your-change
```

3. Install the project dependencies and run the game locally:

```bash
uv sync
uv run hangman-p
```

4. Run the tests before submitting your change:

```bash
uv run --with pytest pytest
```

5. Commit your changes, push your branch, and open a pull request against the
   `main` branch of this repository.

### Author
Mayowa Pitan

# Enjoy your Hangman experience and try not to be hanged...
good luck...
