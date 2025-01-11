"""Rock Scissors Paper Game.

A tiny text-based implementation of the classic Rock, Paper, Scissors game.
"""

from random import choice

HAND_MAP = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
player_score, computer_score = 0, 0

while (player := input("Rock, Paper, or Scissors? ['Q' to quit]: ").lower().strip()) != 'q':
    if player in HAND_MAP:
        computer = choice(list(HAND_MAP.keys()))
        print(f"PLAYER: {player.title()} | COMPUTER: {computer.title()}")
        if player == computer:
            print("DRAW\n")
        elif HAND_MAP[player] == computer:
            player_score += 1
            print("YOU WIN!\n")
        else:
            computer_score += 1
            print("YOU LOSE!\n")
        print(f"SCORE: Player {player_score} | Computer {computer_score}")
    else:
        print(f"{player} is not valid! Try again!\n")

print(f"Final Score: Player {player_score} | Computer {computer_score}")
