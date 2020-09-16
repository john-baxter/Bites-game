from constants import K_COLOUR_V_FOOD_DICT
from constants import K_FOOD_V_COLOUR_DICT

class Player():
  def __init__(self, name):
    """Initialises an instance of the Player class

    Arguments
    ---------
    name : (string)
      The name of the player
    
    Attributes
    ----------
    hand : (dict)
      An empty dictionary ready to be populated with the food tokens collected by the player during the game
      keys will be the ID of the food as strings
      values will be the number of that food as integers

    score : (integer)
      A record of the points scored by this player
    """
    self.name = name
    self.hand = self.initialise_hand()
    self.score = 0

  def initialise_hand(self):
    """Generates the player's hand at the start of the game
    The hand will be empty, ready to be populated with food tokens as 
    the player collects them through the game.

    Returns
    -------
    hand : (dict)
      An empty dictionary ready to be populated with the food tokens collected by the player during the game
      keys will be the ID of the food as strings
      values will be the number of that food as integers
    """
    hand = {}
    return hand

  def store_food(self, food):
    """Places collected token into player's hand
    Increments the number of a given food type; or if not already present, 
    adds food type to hand.

    Updates
    -------
    hand : (dict)
      Dictionary of all food tokens held by the player at tyhe current time. 
      will be used to calculate score at end of game.
      Keys are food types as strings.
      Values are integers.
    """
    if food in self.hand:
      self.hand[food] += 1
    else:
      self.hand[food] = 1
    
  def score_hand(self, anthill):
    """Calculates player's points at the end of the game
    Could be called any time but to reflect the real game there is no running 
    total of points; just a single calculation and comparison after the final ant 
    has reached the anthill.

    Arguments
    ---------
    anthill : (list)
      A list recording which ant is in which spot on the anthill at the end of the game.
      The index of each ant will be used as the value of each of the corresponding 
      food token in a player's hand.
      Each element is a string

    Updates
    -------
    score : (integer)
      An integer showing the player's points total. Will be initialised at 0 and 
      will be updated at the end of the game.
    """
    self.score = 0
    for food in self.hand:
      self.score += anthill.index(K_FOOD_V_COLOUR_DICT[food]) * self.hand[food]

  def choose_ant_to_move(self, allowed_choices):
    """Player chooses which colour of insect meeple to move this turn

    Checks player input against a list of available options.

    Parameters
    ----------
    alowed_choices : (list)
      A list containing the possible options available to the player.
      Elements are the IDs of the ants as strings.

    Returns
    -------
    user_choice : (string)
      The ID of the ant the player has chosen to move
    """
    self.user_choice = None
    while self.user_choice not in allowed_choices:
      self.user_choice = input("Pick something: ")
    return self.user_choice