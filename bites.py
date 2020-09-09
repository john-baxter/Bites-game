import random
from constants import ANTS
from constants import K_COLOUR_V_FOOD_DICT
# from constants import K_FOOD_V_COLOUR_DICT
  
def initialise_ants(ants):
  """Create a record of the starting positions of each insect meeple
  This will show the starting positions as None, since the ants are not 
  positioned on the trail immediately.

  Parameters
  ----------
  ants : (list)
    A list containing the ID of each ant, refered to by colour
    The list can be found at constants.py/ANTS
    Each element is a string

  Returns
  -------
  ant_positions : (dict)
    A dictionary showing the starting location of each ant.
    Initially set as None, the position will be changed throughout the game as 
    the ant moves along the trail, the position on the trail will be defined as the 
    index of the element in the trail list, from initialise_trail
    Keys are strings
    Values are integers
  """
  ant_positions = {}
  for ant in ants:
    ant_positions[ant] = None
  return ant_positions
  
def initialise_trail(foods):
  """Create the path of tokens that the game is played on
  
  Parameters
  ----------
  foods : (dict)
    Each type of food token to be used, and their quantities
    The names of the foods are strings
    The quantities are integers
  
  Returns
  -------
  trail : (list)
    A random shuffled list of all the tokens given in the foods argument
    Each element is a string.
  """
  trail = []
  for food, amount in foods.items():
    trail = trail + ([food] * amount)
  random.shuffle(trail)
  return trail

def move_ant(trail, ant_positions, ant):
  """Move an insect meeple along the board.
  The selected ant moves to the next available food token of its own colour.

  Parameters
  ----------
  trail : (list of strings)
    The trail contains a list of the food tokens available on the game area.
    The types of food token can be found in constants.py/FOOD_TYPES
    As food tokens are removed from the game the elements are replaced with None

  ant_positions : (dict)
    A dictionary showing which element of the trail list each ant is positioned at.

  ant : (string)
    The ant which the player has chosen to move this turn.
    The list of possible ant IDs can be found at constants.py/ANTS
    ...should be one of the keys in ant_positions

  Returns
  -------
  ant_positions : (dict)
    An updated version of the input ant_positions dictionary 
    with the moved ant showing in its new position
  """
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

def take_food(trail, ant_positions, ant, direction):
  """Collect a token from the game path
  Allows the user to choose what food token to collect after moving an ant.
  Replaces the removed token with None; keeping the length of the 
  trail consistent through the game.

  Parameters
  ----------
  trail : (list)
    The shuffled list of all food tiles being used in the game; 
    will be interspersed with None at indices where food has already been collected
    Each element is a string
  
  ant_positions : (dict)
    A dictionary showing the starting location of each ant.
    The position on the trail will be defined as the index of the 
    element in the trail list.
    Keys are strings
    Values are integers

  ant : (string)
    The ID of the ant which has been moved by the user
  
  direction : (string)
    The user's choice of which food token to collect.
    Can be either 'front' or 'back'

  Returns
  -------
  food_to_hand : (string)
    The food token chosen by the user.

  trail : (list)
    The newly updated list of food tokens being used in the game; 
    with the user's chosen token having been replaced with None.

  Raises
  ------
  ValueError
    If the user enters something other than 'front' or 'back' when 
    indicating choice of direction.
  """
  food_position = ant_positions[ant]

  if direction == "front":
    variation = 1
  elif direction == "back":
    variation = -1
  else:
    raise(ValueError("Direction should be 'front' or 'back'."))

  while food_position in ant_positions.values():
    food_position = food_position + variation

  food_to_hand = trail[food_position]
  trail[food_position] = None

  return (food_to_hand, trail)

def initialise_anthill(ants):
  """Create the ending position for the insect meeple ready for the end of the path

  Parameters
  ----------
  ants : (list)
    A list containing the ID of each ant, refered to by colour
    The list can be found at constants.py/ANTS
    Each element is a string
  
  Returns
  -------
  anthill : (list)
    A list of equivalent length to the ants parameter, initially populated with each 
    element as None; ready to be filled with the ID (string) of each ant as they reach 
    the end of the trail.
  """
  anthill = [None] * len(ants)
  return anthill

def place_ant_on_anthill(anthill, ant):
  """Insect meeple goes on correct level of home structure

  Places ant onto appropriate step of the anthill structure when it travels beyond 
  the end of the trail. This determines how many points the corresponding food tokens 
  will be worth.

  Parameters
  ----------
  anthill : (list)
    A list with the same length as the number of ants in the game. 
    Initialised with each element as None.
    Elements will be changed into the IDs of the ants as they reach the anthill.
    Each element is None or string.

  ant : (string)
    The ID of the ant which is being placed onto the anthill.

  Returns
  -------
  anthill : (list)
    Newly updated version of the anthill list; showing one fewer None and one more 
    ant ID (string) in the appropriate place.
  """
  for i in range(len(anthill)-1, -1, -1):
    if anthill[i] is not None:
      continue
    else:
      anthill[i] = ant
      break

  return anthill
