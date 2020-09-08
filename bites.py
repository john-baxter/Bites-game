import random
from constants import K_COLOUR_V_FOOD_DICT
# from constants import K_FOOD_V_COLOUR_DICT
  
def initialise_ants(ants):
  ant_positions = {}
  for ant in ants:
    ant_positions[ant] = None
  return ant_positions
  
def initialise_trail(foods):
  trail = []
  for food, amount in foods.items():
    trail = trail + ([food] * amount)
  random.shuffle(trail)
  return trail

def move_ant(trail, ant_positions, ant):
  """Move a game piece along the board.
  The ant moves to the next available food token of its own colour.

  Parameters:
  -----------
  trail : (list of strings)
    The trail contains a list of the food tokens available on the game area.
    The types of food token can be found in ...
    As food tokens are removed from the game the elements are replaced with None

  ant_positions : (dict)
  
  ant : (string)

  Returns:
  --------
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
  anthill = [None] * 5
  return anthill
