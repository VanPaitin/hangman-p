from random import choice
import pytest

from hangman_p.game_engine import GameEngine
from hangman_p.game_persistence import GamePersistence
from hangman_p.project import game_actions, get_level, get_challenger
from hangman_p import level
from hangman_p.utilities import get_valid_choice, name_validator, VALID



def test_game_actions():
    assert game_actions() == ['p', 'P', 'play', 'i', 'I', 'instruction', 'q', 'Q', 'quit', 'l', 'L', 'load']


def test_get_level(monkeypatch, capsys):
    config = level.Level.config
    # test single player
    difficulty = choice(['1', '2', '3'])
    answers = iter([
        '2', # option= '2' => single player
        difficulty
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    lvl = get_level("Mayowa")

    out = capsys.readouterr().out

    assert f'Welcome Mayowa, In this level, you will have {lvl.chances} chances to guess' in out

    assert lvl.difficulty == difficulty
    assert lvl.player == 'Mayowa'
    assert lvl.challenger == None
    assert lvl.min == config[difficulty]['min']
    assert lvl.max == config[difficulty]['max']
    assert lvl.chances == config[difficulty]['chances']

    # test multiplayer
    answers = iter([
        '1', # option= '1' => multi player
        '1', # difficulty of 1
        'Femi',
        'Mayowa'
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    monkeypatch.setattr(level, 'askpass', lambda _: 'secret')

    lvl = get_level('Mayowa')
    out = capsys.readouterr().out

    assert f'Welcome Femi, In this level, you will have {lvl.chances} chances to guess' in out
    assert lvl.difficulty == '1'
    assert lvl.player == 'Femi'
    assert lvl.challenger == 'Mayowa'
    assert lvl.min == config['1']['min']
    assert lvl.max == config['1']['max']
    assert lvl.chances == config['1']['chances']


def test_get_challenger(monkeypatch):
    answers = iter(['Wrongname', 'incorrect', 'invalid', 'Mayowa'])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    # It should only return any of the passed in arguments
    challenger = get_challenger('Mayowa', 'Tunde')

    assert challenger == 'Mayowa'


def test_name_validator():
    assert name_validator("Mayowa Pitan") == VALID
    assert name_validator("Mayowa-Temi") == VALID

    valid, error = name_validator("Mayowa123")

    assert valid is False
    assert "Please enter a real name" in error


def test_get_valid_choice_reprompts_until_valid(monkeypatch):
    answers = iter(["maybe", "YES"])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    assert get_valid_choice(["yes", "no"]) == "YES"


def test_game_engine_tracks_guesses_and_progress(capsys):
    engine = GameEngine(chances=5, game_word="apple", player="Mayowa")

    assert engine.word_control == "_____"
    assert engine.attempts == 0

    engine._compare_guess("p")
    engine._compare_guess("z")

    assert engine.word_control == "_pp__"
    assert engine.attempts == 2
    assert engine.is_game_won is False
    assert "Nice one!" in capsys.readouterr().out


def test_game_engine_validates_repeated_and_invalid_guesses():
    engine = GameEngine(chances=5, game_word="apple", player="Mayowa")
    engine._right_guesses.add("a")

    assert engine.guess_validator("b") == VALID

    valid, error = engine.guess_validator("a")
    assert valid is False
    assert "used a already" in error

    valid, error = engine.guess_validator("apple")
    assert valid is False
    assert error == "Enter just one character please: "


def test_level_generate_word_uses_packaged_dictionary(monkeypatch):
    lvl = level.Level.__new__(level.Level)
    lvl.min = 4
    lvl.max = 8

    monkeypatch.setattr(level, "choice", lambda words: words[0])

    word = lvl.generate_word()

    assert isinstance(word, str)
    assert 4 <= len(word) <= 8


def test_game_persistence_saves_and_deletes_games(tmp_path, monkeypatch):
    engine = GameEngine(chances=5, game_word="apple", player="Mayowa")
    save_file = tmp_path / "saved_games.pkl"

    monkeypatch.setattr(GamePersistence, "save_dir", tmp_path)
    monkeypatch.setattr(GamePersistence, "saved_games", save_file)
    monkeypatch.setattr(GamePersistence, "engines", [engine])

    GamePersistence._save_all()

    loaded_games = GamePersistence.load_all()

    assert len(loaded_games) == 1
    assert loaded_games[0].player == "Mayowa"
    assert loaded_games[0].word_control == "_____"

    GamePersistence.delete_game(engine)

    assert GamePersistence.engines == []
    assert GamePersistence.load_all() == []


def test_game_persistence_load_all_handles_missing_and_bad_files(tmp_path, monkeypatch):
    save_file = tmp_path / "saved_games.pkl"

    monkeypatch.setattr(GamePersistence, "saved_games", save_file)

    assert GamePersistence.load_all() == []

    save_file.write_text("not a pickle")

    assert GamePersistence.load_all() == []


def test_level_rejects_invalid_difficulty():
    with pytest.raises(ValueError, match="Invalid Value"):
        level.Level("4", "Mayowa")
