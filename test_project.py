from random import choice
from project import game_actions, get_level, get_challenger
import level



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
