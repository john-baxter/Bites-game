import random
from constants import ANTS
from constants import K_COLOUR_V_FOOD_DICT
# from constants import K_FOOD_V_COLOUR_DICT
  
def initialise_ants(ANTS):
  """Create a record of the starting positions of each insect meeple
  This will show the starting positions as None, since the ants are not 
  positioned on the train immediately.

  Parameters
  ----------
  ANTS : (list)
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
  ants = ANTS
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
  Replaces the removed token with None; keeping the lenght of the 
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

  unnamed_tuple : (tuple)
    A two-element tuple containing the return values of this function
    element[0] is food_to_hand
    element[1] is trail

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

def initialise_anthill():
  """Create the ending position for the insect meeple ready for the end of the path

  Returns
  -------
  anthill : (list)
    A list of length five, initially populated with each element as None; 
    ready to be filled with the ID (string) of each ant as they reach the 
    end of the trail.
  """
  anthill = [None] * 5
  return anthill
