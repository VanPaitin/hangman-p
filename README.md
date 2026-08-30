# Hangman

[![CI](https://github.com/VanPaitin/hangman-p/actions/workflows/pylint.yml/badge.svg)](https://github.com/VanPaitin/hangman-p/actions/workflows/pylint.yml)

## Description

**Hangman** is a command-line word-guessing game implemented in Python. Players
guess a hidden word one letter at a time before running out of attempts. The game
supports multiple difficulty levels, saved games, and a multiplayer challenge
mode.

This project demonstrates object-oriented design, input validation, persistence
with `pickle`, modular architecture, and automated testing with `pytest`.

## Demo

![Hangman terminal demo](https://raw.githubusercontent.com/VanPaitin/hangman-p/main/hangman.gif)

## Features

- Three difficulty levels with different word lengths
- Single-player and multiplayer modes
- Game saving and loading in single-player mode
- Automatic deletion of completed saved games
- Input validation and error handling
- Automatic display of numbers, spaces, and punctuation in hidden words
- Automated tests with `pytest`
- Interactive command-line gameplay

## Installation

To install the game with `uv`:

```bash
uv tool install hangman-p
```

This installs the game in an isolated environment and makes the `hangman-p`
command available on your `PATH`.

You can also try the game without permanently installing it:

```bash
uvx --from hangman-p hangman-p
```

To install it into your active Python environment with `pip`:

```bash
python -m pip install hangman-p
```

## Usage

Hangman is an interactive terminal game. After installation, start it with:

```bash
hangman-p
```

You can also run it as a Python module:

```bash
python -m hangman_p
```

## How to play

> Welcome to Hangman, the no-nonsense game. Be smart, then you live. If not,
> you'll have to die by hanging.

The main menu gives you four options:

- Press `P` or enter `play` to start a game.
- Press `I` or enter `instruction` to read the instructions.
- Press `L` or enter `load` to continue a saved game.
- Press `Q` or enter `quit` to leave the game.

When you start a game, choose a difficulty level and either play against the
computer or challenge another player. The hidden word is represented by
underscores, with one underscore for each letter. Numbers, spaces, and
punctuation are displayed automatically.

Guess one letter at a time. A correct guess reveals every matching position in
the word. You win by revealing all the letters within the available number of
attempts. Failure means death by hanging.

### Multiplayer note

When the challenger enters the secret word, the input is masked so the guessing
player cannot see it.

### Extra commands

| Command           | Action                                                                     |
| ----------------- | -------------------------------------------------------------------------- |
| `:c`              | Reveal the secret word. This is a cheat, so use it wisely.                 |
| `:h` or `history` | Display your correct and incorrect guesses.                                |
| `:q` or `quit`    | Quit the current game. In single-player mode, you can save before leaving. |

## Project structure

```bash
project.py                     # Compatibility wrapper
hangman_p/project.py           # Packaged CLI entry point
hangman_p/level.py             # Difficulty configuration
hangman_p/game_engine.py       # Core gameplay logic
hangman_p/dictionary.txt       # Word list for single-player mode
hangman_p/game_persistence.py  # Saved-game handling
pyproject.toml                 # Package metadata and dependencies
test_project.py                # Automated tests
```

## Design decisions

- **Encapsulated game state:** I selected an object-oriented design so each game
  engine can own and manage changing state, including the hidden word, guesses,
  remaining attempts, and player information.
- **Object persistence:** I chose `pickle` to serialize complete game objects
  and restore them when a player continues a saved game.
- **Reusable input validation:** I extracted the validation logic into the
  reusable
  [`cli-input-validator`](https://pypi.org/project/cli-input-validator/)
  package instead of duplicating it throughout the game.
- **Testable terminal input:** I used dependency injection where the game needs
  a custom input function, such as masked input, and `pytest` monkeypatching to
  test interactive input and output without requiring a live terminal session.

## Project history

Hangman began as my CS50P final project and has since evolved into an
installable, tested CLI package published on PyPI. You can watch the
[original project demo](https://youtu.be/2FduPPZd-YU).

## Contributing

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

## Author

Mayowa Pitan

> **Enjoy your Hangman experience and try not to be hanged.**
>
> Good luck!
