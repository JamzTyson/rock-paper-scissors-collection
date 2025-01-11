"""Pytests for Config class."""

import string
from dataclasses import FrozenInstanceError
from enum import Enum

import pytest

from rock_scissors_paper.play import Config, Hand


def test_hand():
    """Ensure that Hand Enums contain expected name / value pairs.

    This test should run before other tests as the Config() class
    is tightly coupled to the Hand Enums.
    """
    class ExpectedHand(Enum):
        """Hand Enums."""
        ROCK = 'Rock'
        SCISSORS = 'Scissors'
        PAPER = 'Paper'

    for actual, expected in zip((Hand), (ExpectedHand)):
        assert actual.name == expected.name
        assert actual.value == expected.value


@pytest.fixture
def config():
    """Fixture for creating a Config instance."""
    return Config()


def test_default_quit_key(config):
    """Ensure the default quit key is a single uppercase letter."""
    assert config.quit_key in string.ascii_uppercase


def test_hand_names(config):
    """Ensure the default hand names are ROCK, SCISSORS, PAPER (Enums)."""
    expected_hands = (Hand.ROCK, Hand.SCISSORS, Hand.PAPER)
    assert config.hand_names == expected_hands


def test_choice_map(config):
    """Ensure that Config.choice_map maps keys to all valid Hands."""
    mapped = set(value for value in config.choice_map.values())
    assert mapped == set(config.hand_names)


def test_choice_map_values(config):
    """Ensure that each key in choice_map maps to a Hand Enum."""
    for key in config.choice_map.keys():
        assert config.choice_map[key] in Hand


def test_beats_map(config):
    """Ensure that Config.beats_map maps keys to all valid Hands."""
    mapped = set(value for value in config.beats_map.values())
    assert mapped == set(config.hand_names)


def test_beats_map_types(config):
    """Ensure that Config.beats_map keys and values are Hands."""
    for key, value in config.beats_map.items():
        assert key in Hand
        assert value in Hand


def test_beats_map_one_to_one(config):
    """Ensure that each Hand maps to one other Hand qwithout duplicates."""
    key_set = set()
    val_set = set()
    hand_set = set(config.hand_names)
    for key, value in config.beats_map.items():
        assert key != value, f"{key} beats itself, which is invalid."
        key_set.add(key)
        val_set.add(value)
    assert key_set == hand_set, "beats_map keys do not match hand_name values."
    assert val_set == hand_set, "beats_map values do not match hand_name values."


def test_immutable(config):
    """Ensure all attributes are immutable."""
    with pytest.raises(FrozenInstanceError):
        config.quit_key = 'X'

    # Ensure hand_names (tuple) is immutable.
    with pytest.raises(FrozenInstanceError):
        config.hand_names = (Hand.NONE,)

    # Ensure the maps are immutable.
    with pytest.raises(TypeError):
        # Ensure we cannot modify a value.
        config.choice_map['1'] = Hand.PAPER
    with pytest.raises(TypeError):
        # Ensure we cannot add another key value pair.
        config.choice_map['4'] = Hand.ROCK
    with pytest.raises(TypeError):
        # Ensure we cannot modify a value.
        config.beats_map['Hand.ROCK'] = Hand.PAPER
    with pytest.raises(TypeError):
        # Ensure we cannot add another key value pair.
        config.choice_map[''] = Hand.NONE
