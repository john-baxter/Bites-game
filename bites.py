import random

def initialise_ants(ants):
  ant_positions = {}
  for ant in ants:
    ant_positions[ant] = None
  return ant_positions
  
def initialise_path(foods):
  path = []
  for food, amount in foods.items():
    path = path + ([food] * amount)
  random.shuffle(path)
  return path

def initialise_hand():
  hand = {}
  return hand
