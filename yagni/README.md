# Rock, Scissors, Paper

A simple Python implementation of the classic game "Rock, Scissors, Paper" for the terminal.

## Features

- Play against the computer, which randomly chooses between rock,
scissors, or paper.
- A minimalistic design following the YAGNI (You Aren't Gonna Need It)
principle.
- Object-oriented design.
- Simple terminal-based UI (no graphics—just text!).

## Requirements

Python 3.12

## Installation

1. Clone the repository:

```bash
git clone git@github.com:JamzTyson/RSP_YAGNI.git
```

2. Navigate to the project directory:

```bash
cd rock_scissors_paper
```

## Usage

Run the game with the following command:

```bash
python3 play.py
```

The game will prompt you to enter your choice (rock, paper, or scissors),
and the computer will randomly choose its move. After each round, the result
will be displayed, and the game will ask if you'd like to play again.

**Example**

```bash
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

Enter your name: james
Press Enter to play or Q to quit:
```

```bash
James: 0 | Computer: 0
1: Rock, 2: Scissors, 3: Paper: 2
```

```bash
James played Scissors | Computer played Paper
Scissors beats Paper. You Win
James: 1 | Computer: 0

Press Enter to play or Q to quit: 
```

## How It Works

The game randomly generates the computer's choice from the options
"rock", "scissors", or "paper".

It then compares the player’s choice to the computer’s:

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.

The winner is displayed, and the game continues until the player quits.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
