"""A simple yet modular implementation of Rock, Scissors, Paper."""

import os
import sys
from dataclasses import dataclass
from enum import auto, Enum
from random import choice
from types import MappingProxyType

INSTRUCTIONS = """
Welcome to Rock, Scissors, Paper!

How to Play:

To make your choice, type:
    - 1 for Rock
    - 2 for Scissors
    - 3 for Paper

Rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock
    - If both players choose the same option, it's a draw.
"""


class Result(Enum):
    """Result Enums."""
    WIN = auto()
    LOSE = auto()
    DRAW = auto()


class Hand(Enum):
    """Hand Enums."""
    ROCK = 'Rock'
    SCISSORS = 'Scissors'
    PAPER = 'Paper'
    NONE = ''

    def __str__(self):
        """Printable value."""
        return self.value


@dataclass(frozen=True)
class Config:
    """Game configuration."""
    quit_key: str = 'Q'
    hand_names: tuple[Hand, ...] = (Hand.ROCK, Hand.SCISSORS, Hand.PAPER)
    choice_map: MappingProxyType = MappingProxyType(
        {'1': Hand.ROCK, '2': Hand.SCISSORS, '3': Hand.PAPER})
    beats_map: MappingProxyType = MappingProxyType(
        {Hand.ROCK: Hand.SCISSORS,
         Hand.SCISSORS: Hand.PAPER,
         Hand.PAPER: Hand.ROCK})


@dataclass
class GameState:
    """Game state container.

    Attributes:
        player_name (str): The player's name.
        player_hand (Hand): The player's current hand choice.
        computer_hand (Hand): The computer's current hand choice.
        player_score: (int): The player's current score.
        computer_score: (int): The computer's current score.
        result (Enum): Result of the most recent round.
    """

    player_name: str = ''
    player_hand: Hand = Hand.NONE
    computer_hand: Hand = Hand.NONE
    player_score: int = 0
    computer_score: int = 0
    result: Result = Result.DRAW


class UI:
    """User interface via Terminal."""
    def __init__(self, config: Config, game_state: GameState) -> None:
        """Initialise user interface."""
        self._game_state = game_state  # shared state.
        # Player name does not change during game, so we only need to set it once.
        self._player_name = game_state.player_name
        self._config = config

    def get_player_choice(self) -> Hand:
        """Return player's selected choice."""
        while True:
            user_input = input("1: Rock, 2: Scissors, 3: Paper: ")
            if hand := self._config.choice_map.get(user_input):
                return hand
            print("Choice must be: 1, 2 or 3.")

    def print_scores(self) -> None:
        """Print scores."""
        print(f"{self._player_name}: {self._game_state.player_score} | "
              f"Computer: {self._game_state.computer_score}")

    def display_result(self) -> None:
        """Print the winner."""
        player_hand = self._game_state.player_hand
        computer_hand = self._game_state.computer_hand

        summary = (f"{self._player_name} played {player_hand} | "
                   f"Computer played {computer_hand}")

        result_message = {
            Result.DRAW: f"You both chose {player_hand}. Draw",
            Result.WIN: f"{player_hand} beats {computer_hand}. You Win",
            Result.LOSE: f"{player_hand} is beaten by {computer_hand}. You Lose"
        }

        # Render output messages.
        clear_screen()
        print(summary)
        print(result_message[self._game_state.result])
        self.print_scores()
        print()  # Empty line.

    def display_end_screen(self) -> None:
        """Display final score and farewell message."""
        player_score = self._game_state.player_score
        computer_score = self._game_state.computer_score

        if player_score == computer_score:
            result_message = "The game was a DRAW!"
        elif player_score > computer_score:
            result_message = f"{self._player_name} WON!"
        else:
            result_message = f"{self._player_name} LOST!"

        clear_screen()
        print("The final score is:")
        self.print_scores()
        print(result_message)
        print("Bye.")

    def prompt_to_continue(self) -> bool:
        """Return True if users chooses to quit game."""
        user_input = input("Press Enter to play or "
                           f"{self._config.quit_key} to quit: ")
        return user_input.strip().upper() != self._config.quit_key


class Game:
    """Manage the logic and game state of Rock Scissor Paper game."""
    def __init__(self, name: str, config: Config) -> None:
        self._config = config
        self._game_state = GameState(player_name=name)

    @property
    def game_state(self) -> GameState:
        """Return current game state."""
        return self._game_state

    def set_computer_choice(self) -> None:
        """Set random computer_hand from hand_names."""
        self._game_state.computer_hand = choice(self._config.hand_names)

    def update_scores(self) -> None:
        """Update scores after both players have chosen."""
        player_hand = self._game_state.player_hand
        computer_hand = self._game_state.computer_hand
        beats_map = self._config.beats_map

        if player_hand == computer_hand:
            result = Result.DRAW
        elif beats_map[player_hand] == computer_hand:
            result = Result.WIN
            self._game_state.player_score += 1
        else:
            result = Result.LOSE
            self._game_state.computer_score += 1

        self._game_state.result = result

    def play_round(self, player_hand: Hand) -> None:
        """Handle player wins hand.

        Args:
            player_hand (str): The human player's chosen hand.
        """
        self._game_state.player_hand = player_hand
        self.set_computer_choice()
        self.update_scores()


def clear_screen() -> None:
    """Clear the terminal screen or fallback to printing a newline."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    elif 'TERM' in os.environ:  # Unix-like with terminal support
        os.system('clear')
    else:  # Fallback
        print('\n')


def play(user_name: str) -> None:
    """Main game loop.

    Args:
        user_name (str): The human player's name.
    """
    config = Config()
    game = Game(user_name, config)
    ui = UI(config, game.game_state)

    while ui.prompt_to_continue():
        clear_screen()
        ui.print_scores()
        game.play_round(ui.get_player_choice())
        ui.display_result()
    ui.display_end_screen()
    sys.exit(0)


if __name__ == '__main__':
    print(INSTRUCTIONS)
    try:
        play(input("Enter your name: ").title())
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit(0)
