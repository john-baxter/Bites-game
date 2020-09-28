import random
from constants import K_COLOUR_V_FOOD_DICT

class Bites():
  def __init__(self, ants, tokens_for_trail, players):
    """Initialises an instance of the Bites class

    This is the equivalent of setting up the game on the table ready to start playing.

    Arguments
    ---------
    ants : (list)
      The list of the ants which will be used for the game. 
      Each element is a string.

    tokens_for_trail : (dict)
      The names of each type of food token and their quantities
      The keys are names of food as strings.
      The values are the amount of the food as integers.

    players : (list)
      A list of Player objects representing the players of this game.
      Elements are instances of the Player class
    
    Attributes
    ----------
    ant_positions : (dict)
      The current position of each ant
      Initialised with each position as None and will be updated through the 
      game refering to the index of the trail list element the ant is positioned at.
      Keys are ant IDs as strings
      Values are integers or None

    trail : (list)
      A random shuffled list of all the tokens given in the tokens_for_trail argument
      Each element is a string.

    anthill : (list)
      A list of equivalent length to the ants parameter, initially populated with each 
      element as None; ready to be filled with the ID (string) of each ant as they reach 
      the end of the trail.

    players : (list)
      A list of Player objects representing the players of this game.
      Elements are instances of the Player class
    """
    self.ant_positions = self.initialise_ants(ants)
    self.trail = self.initialise_trail(tokens_for_trail)
    self.anthill = self.initialise_anthill(ants)
    self.players = players

  def initialise_ants(self, ants):
    """Create a record of the starting positions of each insect meeple
    This will show the starting positions as None, since the ants are not 
    positioned on the trail immediately.

    Parameters
    ----------
    ants : (list)
      A list containing the ID of each ant, refered to by colour
      The list can be found at constants.ANTS
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
  
  def initialise_anthill(self, ants):
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
  
  def initialise_trail(self, tokens_for_trail):
    """Create the path of tokens that the game is played on
    
    Parameters
    ----------
    tokens_for_trail : (dict)
      Each type of food token to be used, and their quantities
      The names of the foods are strings
      The quantities are integers
    
    Returns
    -------
    trail : (list)
      A random shuffled list of all the tokens given in the tokens_for_trail argument
      Each element is a string.
    """
    trail = []
    for food, amount in tokens_for_trail.items():
      trail = trail + ([food] * amount)
    random.shuffle(trail)
    return trail

  def play(self):
    (self.trail, self.ant_positions, self.anthill) = \
      self.players[0].take_turn(
        self.trail, self.ant_positions, self.anthill)
