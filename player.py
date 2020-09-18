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
    name : (string)
      Each player will be identified by their name

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
      Dictionary of all food tokens held by the player at the current time. 
      Will be used to calculate score at end of game.
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

    Addresses player by name and asks them for their choice of ant.
    Checks player input against a list of available options.

    Parameters
    ----------
    allowed_choices : (list)
      A list containing the possible options available to the player.
      Elements are the IDs of the ants as strings.

    Returns
    -------
    user_choice_ant : (string)
      The ID of the ant the player has chosen to move
    """
    self.user_choice_ant = None
    while self.user_choice_ant not in allowed_choices:
      self.user_choice_ant = input("%s; please enter your choice of ant: " % self.name)
    return self.user_choice_ant

  def choose_direction_to_pick_food(self, allowed_choices):
    """Player chooses which direction to collect food token from.

    Addresses player by name and asks them for their chosen direction.
    Player choice will be relative to the ant's new position immediately 
    after a movement.
    Checks player input against a list of available options.

    Parameters
    ----------
    allowed_choices : (list)
      A list containing the possible options available to the player.
      Elements are the IDs of the ants as strings.

    Returns
    -------
    user_choice_direction : (string)
      The user's choice of which direction to collect the food token from.
   """
    self.user_choice_direction = None
    while self.user_choice_direction not in allowed_choices:
      self.user_choice_direction = input("%s; please pick a direction to collect food from: " % self.name)
    return self.user_choice_direction

  def move_ant_along_trail(self, trail, ant_positions, ant):
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

  def place_ant_on_anthill(self, ant_positions, anthill, ant):
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

    ant_positions[ant] = "anthill"
    
    return (anthill, ant_positions)

  def take_food_from_trail(self, trail, ant_positions, ant, direction):
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

  def move_ant(self, trail, ant_positions, anthill, ant):
    if ant_positions[ant] is None:
      return_tuple = (anthill, self.move_ant_along_trail(trail, ant_positions, ant))
    elif K_COLOUR_V_FOOD_DICT[ant] not in trail[ant_positions[ant]+1:]:
      return_tuple = self.place_ant_on_anthill(ant_positions, anthill, ant)
    else:
      return_tuple = (anthill, self.move_ant_along_trail(trail, ant_positions, ant))
    
    return return_tuple
