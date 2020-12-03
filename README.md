# Bites-game
## Code written by John Baxter

[Scope](#scope) / 
[Motivation](#motivation) / 
[Tech](#tech-used) / 
[Features](#features) / 
[Code example](#code-example) / 
[Tests](#tests) / 
[<u>How to use</u>](#how-to-use) / 
[Future development](#future-development) / 
[Credits](#credits) 

## [^](#code-written-by-john-baxter)Scope
This project aims to create a playable clone of the existing tabletop game ['Bites'](https://www.boardgametables.com/products/bites-board-game).

## [^](#code-written-by-john-baxter)Motivation
The motivation to create this project was for me to improve my general understanding of the principles of Test-driven Development (TDD) and Object-oriented Programming (OOP) while also learning the basics of a new language and working on a project that is fun, engaging and more interesting than mindlessly following one of the many tutorials available on YouTube.

<!-- ## Build status -->

<!-- ## Code style -->

<!-- ## Screenshots -->

## [^](#code-written-by-john-baxter)Tech used
The project is written in Python 3\
In the current state the whole project is using the Python standard library with no additional packages.

## [^](#code-written-by-john-baxter)Features
The project currently has the following features:
- The game is playable using a simple text-based interface in the Command Line
- 2 to 5 players can play at a time
- Standard food tokens and wine used for the trail
- Standard ant colours used
- Players can collect food from the anthill
- Multiple options for anthill filling. The players may choose one or have the game randomly select one for them.
  * Top-down
  * Bottom-up
  * Specific order: 4, 2, 0, 3 then 1
  * User's choice (Not featured in the original game)
- Multiple options for wine-scoring rule. The players may choose one or have the game randomly select one for them
  * "Collector"
  * "Oenophile"


## [^](#code-written-by-john-baxter)Code example
<!-- TO DO (Continuous) -->
<!-- Check that the line ref in this link is correct; it will change if there is any insertion before it in the player.py file. -->
The following example shows the method within the 
[Player class](./player.py#L144) 
which is used after the choice of which ant to move has been made; and is responsible for defining at what position the ant's move will be completed.\
<b>NB</b> The actual method in [player.py](./player.py) file contains internal documentation whach has been ommited from this example for clarity.

```python
def move_ant_along_trail(self, trail, ant_positions, ant):
    if ant_positions[ant] is None:
      ant_positions[ant] = 0
    else:
      ant_positions[ant] += 1
    
    if trail[ant_positions[ant]] == K_COLOUR_V_FOOD_DICT[ant]:
      return ant_positions
    else:
      while trail[ant_positions[ant]] != K_COLOUR_V_FOOD_DICT[ant]:
        ant_positions[ant] += 1

    return ant_positions
```

<!-- ## Installation -->

<!-- ## API reference -->

## [^](#code-written-by-john-baxter)Tests
The whole project has been created using TDD. The tests are written using Python3's built-in testing framework:
- `unittest`

These can be run by:
1. Opening a terminal window and navigating to the repo.
1. Enter the command `python3 -m unittest discover --pattern=*_test.py`.

## [^](#code-written-by-john-baxter)How to use
If you want to try out this game app, the following steps are required.
(Instructions are specific to using a MacOS, other interfaces may require different/analogous steps.)\
You will need to have Python 3.8 installed.

1. Clone this repository to your own machine.
1. Open a terminal window and navigate to the local version of the repo.
1. Enter the command `python3 controller.py`.
1. Follow the on-screen instructions to begin/continue playing.

Use of the app will require an understanding of how to play the game. An overview and downloadable instruction manaual are available [here](https://www.boardgametables.com/products/bites-board-game)

<!-- ## Contribute
Please don't arse about with it this is my project. -->

## [^](#code-written-by-john-baxter)Future development
Information regarding which features will be added in the future can be found [here](./backlog.md).

## [^](#code-written-by-john-baxter)Credits
Original game by Brigitte Ditt & Wolfgang Ditt.\
Original artwork by Anca Gavril & Filip Gavril.\
Software architecture and Technical leadership by Ana Andrés.

<!-- ## License -->
