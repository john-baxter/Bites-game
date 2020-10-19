# Bites-game

<!-- #### A game by Brigitte Ditt, Wolfgang Ditt, Anca Gavril & Filip Gavril
#### Software architecture & Technical leadership by Ana Andres -->
### Code written by John Baxter

## Scope
This project aims to create a playable clone of the existing tabletop game ['Bites'](https://www.boardgametables.com/products/bites-board-game).

The programming language will be Python. This will serve as an introduction to a new language while working on a project that is fun and interesting.

<!-- ## MVP
The basic game will be playable by at least two players (details about the interface TBD) using basic rules i.e.
  - no chocolate
  - no wine
  - imposed 'Overachiever' setup for anthill level assigning -->

## Motivation
The motivation to create this project was for me to improve my general understanding of the principles of Test-driven Development (TDD) and Object-oriented Programming (OOP) while also learning the basics of a new language and working on a project that is fun, engaging and more interesting than mindlessly following one of the many tutorials available on YouTube.

<!-- ## Build status -->

<!-- ## Code style -->

<!-- ## Screenshots -->

## Tech used
The project is written in Python 3\
In the current state the whole project is using the Python standard library with no additional packages.

## Features
The project currently has the following features:
- The game is playable using a simple text-based interface in the Command Line
- 2 to 5 players can play at a time
- Standard food tokens used for the trail
- Standard ant colours used
- Players can collect food from the anthill
- Ants fill the anthill from top to bottom

## Code example
The following example shows the method within the 
<!-- [Player class](./player.py)  -->
[Player class](./player.py#L142) 
<!-- [Player class](./player.py Player.move_ant_along_trail) -->
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

## Installation

## API reference

## Tests

## How to use

## Contribute

## Credits

## License
