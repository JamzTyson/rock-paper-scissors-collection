# rock-paper-scissors-collection

![Rock Paper Scissors image](https://raw.githubusercontent.com/JamzTyson/Rock_Scissors_Paper/main/assets/rsp.png)

A collection of "Rock Scissors Paper" game implementations  written in Python.

This collection includes minimalist designs, modular frameworks, and
YAGNI-inspired approaches. Although it was primarily written as a learning
project, I hope that other learners, developers, and hobbyists interested in
Python development may find it instructive. 

The collection was written as part of my ongoing journey into Python
programming. As a relatively new Python developer, I have focused on best
practices such as docstrings, type annotations, good code style, unit tests,
and linters. Additionally, I've worked with a modern toolchain (including
PyCharm, Poetry, pylint, flake8, MyPy, GitHub, and PyPi), and have practiced
managing projects from concept to publishing on GitHub and PyPi. These
repositories also represent my growing experience using Git and GitHub,
including working with submodules.

## About the Collection

The Rock-Paper-Scissors Collection serves as a showcase of different design
philosophies and implementation styles for the same problem. Each project
is self-contained, documented, and emphasizes a distinct approach to building
the game.

## Projects Included

### 1. [Rock-Scissors-Paper Tiny](https://github.com/JamzTyson/Rock_Scissors_Paper_tiny)

**Purpose:**

A tiny, structured implementation of the game, focusing on readability and
simplicity.

**Key Features:**

- Minimal codebase (~20 lines).
- Tracks player and computer scores.
- Case-insensitive input handling.
- Designed for quick learning and experimentation.

### 2. [Rock-Scissors-Paper Minimal](https://github.com/JamzTyson/Rock_Scissors_Paper_minimal)

**Purpose:**

A small, text-based game with basic OOP principles.

**Key Features:**

* Introduces player identity (e.g., enter your name).
* Object-oriented design for better structure.
* Simplified but functional gameplay experience.

### 3. [Rock-Scissors-Paper YAGNI](https://github.com/JamzTyson/RSP_YAGNI)

**Purpose:**

A [YAGNI](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)-inspired
implementation avoiding overengineering while maintaining modularity.

**Key Features:**

* Object-oriented design with minimalistic features.
* Simple rules and gameplay.
* Focus on essential functionality and avoiding unnecessary complexity.

### 4. [Rock-Scissors-Paper Framework](https://github.com/JamzTyson/Rock_Scissors_Paper)

**Purpose:**

A highly modular and extendable framework for creating and experimenting with Rock-Paper-Scissors and its variants.

**Key Features:**

* Dynamic rule generation for customizable gameplay.
* Supports adding new choices (e.g., Rock-Paper-Scissors-Lizard-Batman).
* Comprehensive unit tests using Pytest.
* Designed for extensibility and experimentation.

## Getting Started

Each project is standalone and includes its own README.md with detailed
instructions for setup and usage. To get started, simply navigate to the
corresponding repository linked above and follow the instructions provided.

## Prerequisites

- Python 3.x (version specifics vary by project).
- Basic knowledge of terminal usage.

## Cloning the Collection

To clone all projects into a single directory:

    git clone --recurse-submodules https://github.com/JamzTyson/rock-paper-scissors-collection.git

## Exploring Individual Projects

Each project resides in its own folder:

- **Rock_Scissors_Paper_tiny:** [/tiny/](https://github.com/JamzTyson/rock-paper-scissors-collection/tree/main/tiny)
- **Rock_Scissors_Paper_minimal:** [/small/](https://github.com/JamzTyson/rock-paper-scissors-collection/tree/main/small)
- **Rock_Scissors_Paper_YAGNI:** [/yagni/](https://github.com/JamzTyson/rock-paper-scissors-collection/tree/main/yagni)
- **Rock_Scissors_Paper_Framework:** [/framework/](https://github.com/JamzTyson/rock-paper-scissors-collection/tree/main/framework)

Navigate to the desired folder to explore the implementation.

## Contributing

Contributions to the collection or individual projects are welcome!
If you have ideas, improvements, or bug fixes:

* Fork the relevant repository.
* Make your changes.
* Submit a pull request.

## License

All projects in this collection are licensed under the MIT License.
Refer to the individual LICENSE files for more details.
