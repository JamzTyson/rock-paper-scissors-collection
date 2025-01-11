"""Rock Scissors Paper Game.

A simple text-based implementation of the classic Rock, Paper, Scissors game.
"""


from random import choice
from dataclasses import dataclass


CHOICE_MAP = {'r': 'Rock', 's': 'Scissors', 'p': 'Paper'}
BEATS = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}


@dataclass
class Game:
    """Encapsulates game state and logic."""

    player_name: str
    player_score: int = 0
    computer_score: int = 0
    player_hand: str = ''
    computer_hand: str = ''

    def __str__(self):
        """Return the current score and player name in a formatted string."""
        return (f"{self.player_name}: {self.player_score}  "
                f"Computer: {self.computer_score}\n")

    def set_hands(self):
        """Set hand choices for human and computer players."""
        self.computer_hand = choice(list(CHOICE_MAP.values()))

        prompt = "Rock, Scissors or Paper [R, S, P]: "
        while (hand := CHOICE_MAP.get(input(prompt).strip().lower())) is None:
            print("Choice must be one of R, S, or P.")
        self.player_hand = hand

    def adjudicate(self) -> None:
        """Update the scores, and print result from hand comparison."""
        print(f"{self.player_hand} vs {self.computer_hand}")

        if self.player_hand == self.computer_hand:
            print("Draw.")
        elif BEATS[self.player_hand] == self.computer_hand:
            print(f"{self.player_name} wins.")
            self.player_score += 1
        else:
            print(f"{self.player_name} loses.")
            self.computer_score += 1
        print(self)

    def play(self):
        """Run the game loop."""
        while input("Press 'Enter' to play, or 'Q' to quit").lower() != 'q':
            self.set_hands()
            self.adjudicate()
        print(f"Final score: {self}")


def main() -> None:
    """Instantiate game object and call game's play() method."""
    name = input("What is your name? ").title()
    game = Game(player_name=name)
    game.play()


if __name__ == '__main__':
    main()
