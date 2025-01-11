"""Pytests for Game() class."""
from unittest.mock import MagicMock, patch

import pytest

from rock_scissors_paper.play import Config, Game, Hand, Result


@pytest.fixture
def game():
    """Fixture to create a Game instance with a mock player name and a mocked Config."""
    mock_config = MagicMock(spec=Config)
    player_name = "Player"

    # Mock Config attributes
    mock_config.hand_names = (Hand.ROCK, Hand.SCISSORS, Hand.PAPER)
    mock_config.choice_map = {'1': Hand.ROCK, '2': Hand.SCISSORS, '3': Hand.PAPER}
    mock_config.beats_map = {
        Hand.ROCK: Hand.SCISSORS,
        Hand.SCISSORS: Hand.PAPER,
        Hand.PAPER: Hand.ROCK,
    }
    return Game(name=player_name, config=mock_config)


def test_game_initialization(game):
    """Test the initialization of the game state."""
    assert game.game_state.player_name == "Player"
    assert game.game_state.player_hand == Hand.NONE
    assert game.game_state.computer_hand == Hand.NONE
    assert game.game_state.player_score == 0
    assert game.game_state.computer_score == 0
    assert game.game_state.result == Result.DRAW


@patch("rock_scissors_paper.play.choice",
       side_effect=[Hand.ROCK, Hand.SCISSORS, Hand.PAPER])
def test_computer_choice(mock_choice, game):
    """Test that the computer chooses a hand correctly (mocking random.choice.)."""
    game.set_computer_choice()
    assert game.game_state.computer_hand == Hand.ROCK
    game.set_computer_choice()
    assert game.game_state.computer_hand == Hand.SCISSORS
    game.set_computer_choice()
    assert game.game_state.computer_hand == Hand.PAPER

    # choice is called 3 times with hand_names.
    mock_choice.assert_called_with(game._config.hand_names)
    assert mock_choice.call_count == 3


@pytest.mark.parametrize(
    "player, computer, expected_result, expected_score",
    [
        (Hand.ROCK, Hand.SCISSORS, Result.WIN, (1, 0)),  # Player wins
        (Hand.ROCK, Hand.PAPER, Result.LOSE, (0, 1)),  # Player loses
        (Hand.SCISSORS, Hand.SCISSORS, Result.DRAW, (0, 0)),  # Draw
        (Hand.SCISSORS, Hand.PAPER, Result.WIN, (1, 0)),  # Player wins
    ])
def test_update_scores(game, player, computer, expected_result, expected_score):
    """Test score update logic for a win."""
    game.game_state.player_hand = player
    game.game_state.computer_hand = computer
    game.update_scores()
    assert game.game_state.result == expected_result
    assert game.game_state.player_score == expected_score[0]
    assert game.game_state.computer_score == expected_score[1]


@patch("rock_scissors_paper.play.choice", return_value=Hand.SCISSORS)
def test_play_round(mock_choice, game):
    """Test the play_round method."""
    with patch.object(game, 'update_scores') as mock_update_scores:
        game.play_round(Hand.ROCK)  # Player chooses Rock
        assert game.game_state.player_hand == Hand.ROCK
        assert game.game_state.computer_hand == Hand.SCISSORS
        mock_update_scores.assert_called_once()
        mock_choice.assert_called_once_with(game._config.hand_names)
