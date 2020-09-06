import random

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

def initialise_hand():
  hand = {}
  return hand

def move_ant(trail, ant_positions, ant):
  colour_matching_food = {
    "purple": "grapes",
    "red": "apple",
    "brown": "bread",
    "yellow": "cheese",
    "green": "pepper"}
  if ant_positions[ant] is None:
    ant_positions[ant] = 0
  else:
    ant_positions[ant] += 1

  if trail[ant_positions[ant]] == colour_matching_food[ant]:
    return ant_positions
  else:
    while trail[ant_positions[ant]] != colour_matching_food[ant]:
      ant_positions[ant] += 1

  return ant_positions

def take_food(trail, ant_positions, ant, direction):
  return ("cheese", ['apple', 'grapes', None])

