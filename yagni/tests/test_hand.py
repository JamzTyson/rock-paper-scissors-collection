"""Pytests for Hand(Enum) class."""
from rock_scissors_paper.play import Hand


def test_hand_enum_str_representation():
    """Ensure enum string representation matches its value."""
    for hand in Hand:
        assert str(hand) == hand.value
