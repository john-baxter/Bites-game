from constants import K_COLOUR_V_FOOD_DICT
from constants import K_FOOD_V_COLOUR_DICT

class Player():
  def __init__(self):
    self.hand = self.initialise_hand()

  def initialise_hand(self):
    hand = {}
    return hand

  def store_food(self, food):
    if food in self.hand:
      self.hand[food] += 1
    else:
      self.hand[food] = 1
    
  def score_hand(self, anthill):
    score = 0
    for fruit in self.hand:
      score += anthill.index(K_FOOD_V_COLOUR_DICT[fruit]) * self.hand[fruit]
    return score
