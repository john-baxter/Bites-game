from constants import K_COLOUR_V_FOOD_DICT, K_FOOD_V_COLOUR_DICT, STANDARD_FOOD_TYPES
from constants import PROMPT_TEXT_GAME_CHOICE_ANT, PROMPT_TEXT_GAME_CHOICE_DIRECTION, PROMPT_TEXT_GAME_CHOICE_FOOD, PROMPT_TEXT_GAME_CHOICE_ANTHILL_PLACEMENT
from constants import ANTHILL_CARD_DICT, WINE_CARD_DICT, CHOCOLATE_CARD_DICT
from functions import show_allowed_choices_from_list

class Player():
  def __init__(self, name):
    """Initialises an instance of the Player class.

    Parameters
    ----------
    name : (string)
      The name of the player
    
    Attributes
    ----------
    name : (string)
      Each player will be identified by their name

    hand : (dict)
      An empty dictionary ready to be populated with the food tokens collected by the player during the game.
      Keys will be the ID of the food as strings
      Values will be the number of that food as integers

    score : (integer)
      A record of the points scored by this player
    """
    self.name = name
    self.hand = self.initialise_hand()
    self.score = 0

  def initialise_hand(self):
    """Generates the player's hand at the start of the game.
    The hand will be empty, ready to be populated with food tokens as 
    the player collects them through the game.

    Returns
    -------
    hand : (dict)
      An empty dictionary ready to be populated with the food tokens collected by the player during the game.
      Keys will be the ID of the food as strings
      Values will be the number of that food as integers
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
    
  def score_standard_food_in_hand(self, anthill):
    """Calculates player's 'standard' points at the end of the game.

    'Standard' points are those that are acquired through the standard food tokens 
    held by the player.

    Could be called any time but to reflect the real game there is no running 
    total of points; just a single calculation and comparison after the final ant 
    has reached the anthill.

    Parameters
    ----------
    anthill : (list)
      A list recording which ant is in which spot on the anthill at the end of the game.
      The index of each ant will be used as the value of each of the corresponding 
      food token in a player's hand.
      Each element is a string.

    Returns
    -------
    standard_food_score : (integer)
      An integer showing the player's total points from standard food. 
    """
    standard_food_score = 0
    for food in self.hand:
      if food in STANDARD_FOOD_TYPES:
        standard_food_score += anthill.index(K_FOOD_V_COLOUR_DICT[food]) * self.hand[food]
    return standard_food_score

  def make_choice(self, allowed_choices, prompt_text):
    """Used any time the player needs to make a choice

    Addresses player by name and asks them for their choice of ant or food etc.
    Checks player input against a list of available options.

    Parameters
    ----------
    allowed_choices : (list)
      A list containing the possible options available to the player.

    prompt_text : (string)
      A sentence which will prompt the player to make the appropriate choice.

    Returns
    -------
    user_choice : (string)
      The ID of the choice the player has made.
    """
    self.user_choice = None
    show_allowed_choices_from_list(allowed_choices)
    while self.user_choice not in allowed_choices:
      self.user_choice = input("%s; %s: " % (self.name, prompt_text))
    return self.user_choice

  def move_ant_along_trail(self, trail, ant_positions, ant):
    """Move an insect meeple along the board.
    The selected ant moves to the next available food token of its own colour.

    Parameters
    ----------
    trail : (list)
      The trail contains a list of the food tokens available on the game area.
      The types of food token can be found in constants.py/FOOD_TYPES
      As food tokens are removed from the game the elements are replaced with None.
      Elements are strings.

    ant_positions : (dict)
      A dictionary showing which element of the trail list each ant is positioned at.

    ant : (string)
      The ant which the player has chosen to move this turn.
      The list of possible ant IDs can be found at constants.py/ANTS.

    Returns
    -------
    ant_positions : (dict)
      An updated version of the input ant_positions dictionary 
      with the moved ant showing in its new position.
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

  def place_ant_on_anthill(self, ant_positions, anthill, anthill_rule, ant):
    """Insect meeple goes on correct level of home structure

    The method adds ants to the anthill as per the anthill rule currently in play. 
    The method will prompt user for input if appropriate or iterate through anthill 
    indices in the appropriate order to find the correct available location.
    Places ant onto appropriate step of the anthill structure when it travels beyond 
    the end of the trail. This determines how many points the corresponding food tokens 
    will be worth.
    The ant position dictionary will be updated to show the corresponding ant's 
    position as "anthill".

    Parameters
    ----------
    ant_positions : (dict)
      A dictionary with the  positions of the ants along - or not on - the trail of food.
      Keys are ant IDs as strings.
      Values are and position as None or int or "anthill".

    anthill : (list)
      A list with the same length as the number of ants in the game. 
      Initialised with each element as None.
      Elements will be changed into the IDs of the ants as they reach the anthill.
      Each element is None or string.

    anthill_rule : (string)
      The identity of the anthill rule that has been chosen during the setup of the game.

    ant : (string)
      The ID of the ant which is being placed onto the anthill.

    Returns
    -------
    ant_positions : (dict)
      Newly updated dictionary of ant positions.
      Any ants that have been moved onto the anthill will have their positions changed 
      to "anthill".
      Keys are ant IDs as strings.
      Values are and position as None or int or "anthill".

    anthill : (list)
      Newly updated version of the anthill list; showing one fewer None and one more 
      ant ID (string) in the appropriate place.
    """
    if anthill_rule == "user choice":
      i = int(
        self.make_choice(
          self.define_allowed_choices_anthill_placement(anthill), 
          PROMPT_TEXT_GAME_CHOICE_ANTHILL_PLACEMENT
        )
      )
      anthill[i] = ant
    else:
      anthill_rule_list = ANTHILL_CARD_DICT[anthill_rule]
      for i in range(len(anthill)):
        if anthill[anthill_rule_list[i]] is None:
          anthill[anthill_rule_list[i]] = ant
          break

    ant_positions[ant] = "anthill"
    
    return (anthill, ant_positions)

  def take_food_from_trail(self, trail, ant_positions, ant, direction):
    """Collect a token from the game path.

    Allows the user to choose what food token to collect after moving an ant.
    Replaces the removed token with None; keeping the length of the 
    trail consistent through the game.
    Players will be able to take food tokens adjacent to the new position of the ant 
    which has just been moved. 
    Accounts for tokens being unavailable due to presence of ants in adjacent locations 
    or non-existance of tokens (either because the adjacent space is None or because 
    the ant is at a terminal end of the trail so only one token is available.)

    Parameters
    ----------
    trail : (list)
      The shuffled list of all food tiles being used in the game; 
      will be interspersed with None at indices where food has already been collected.
      Each element is a string.
    
    ant_positions : (dict)
      A dictionary showing the starting location of each ant.
      The position on the trail will be defined as the index of the 
      element in the trail list.
      Keys are strings.
      Values are integers.

    ant : (string)
      The ID of the ant which has been moved by the user.
    
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
    """
    food_position = ant_positions[ant]

    if direction == "front":
      variation = 1
    elif direction == "back":
      variation = -1
    else:
      raise(ValueError("Direction should be 'front' or 'back'."))

    while food_position in ant_positions.values() or trail[food_position] is None:
      food_position = food_position + variation

    food_to_hand = trail[food_position]
    trail[food_position] = None

    return (food_to_hand, trail)

  def define_allowed_choices_ants(self, ant_positions):
    """Provides the list of permitted movement options to the player

    Filters out ants that are positioned on the anthill; all other ants are 
    legitimate choices

    Parameters
    ----------
    ant_positions : (dict)
      A dictionary showing the starting location of each ant.
      The position on the trail will be defined as the index of the 
      element in the trail list.
      Keys are strings.
      Values are ant position as None or int or "anthill".

    Returns
    -------
    allowed_choices_ants : (list)
      A list of all ants that are able to be moved, includes any ant that has not 
      yet been moved and any ant which is on the trail. Excludes ants already on the anthill.
      Elements are strings.
    """
    allowed_choices_ants = [k for k, v in ant_positions.items() if v != "anthill"]
    return allowed_choices_ants

  def define_allowed_choices_direction(self, ant, trail, ant_positions):
    """Provides the list of permitted food-picking options to the player.

    Determines whether player can choose food from in front, behind or both.

    Parameters
    ----------
    ant : (string)
      The ID of the ant which is being placed onto the anthill.

    trail : (list)
      The trail contains a list of the food tokens available on the game area.
      The types of food token can be found in constants.py/FOOD_TYPES
      As food tokens are removed from the game the elements are replaced with None.
    
    ant_positions : (dict)
      A dictionary showing the starting location of each ant.
      The position on the trail will be defined as the index of the 
      element in the trail list.
      Keys are strings.
      Values are ant position as None or int or "anthill".

    Returns
    -------
    allowed_choices_direction : (list)
      A list of all directions in which food is available for the player to 
      collect from the trail.
      Elements are strings.
    """
    allowed_choices_direction = []
    
    trail_slice_pre_ant = trail[:ant_positions[ant]]
    trail_slice_post_ant = trail[ant_positions[ant]+1:]

    for idx, food in enumerate(trail_slice_post_ant):
      is_str = type(trail_slice_post_ant[idx]) is str
      has_no_ant = idx + ant_positions[ant] + 1 not in ant_positions.values()
      if is_str and has_no_ant:
        allowed_choices_direction.append("front")
        break

    for idx, food in enumerate(trail_slice_pre_ant):
      is_str = type(trail_slice_pre_ant[idx]) is str
      has_no_ant = idx not in ant_positions.values()
      if is_str and has_no_ant:
        allowed_choices_direction.append("back")
        break

    return allowed_choices_direction

  def take_standard_turn(self, trail, ant_positions, anthill, anthill_rule, anthill_food_tokens):
    """Perform necessary steps to complete one player's move.

    Parameters
    ----------
    trail : (list)
      The shuffled list of all the food tiles being used in the game.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      Dictionary containing the current locations of each ant.
      Keys are ants as strings.
      Values are ant positions as None, int or "anthill" (string).

    anthill : (list)
      List of equivalent length as the number of ants in the game. 
      Shows which (if any) ants have moved past the end of the trail and their positions on the anthill.
      Elements are None or ant IDs as strings.

    anthill_rule : (list)
      A list defining the order in which the anthill should be filled as ants arrive 
      throughout the game. 

    anthill_food_tokens : (dict)
      Contains the record of which and how many of each food token are stored at the anthill.
      Keys are food types as strings.
      Values are integers >=0.

    Returns
    -------
    trail : (list)
      The newly updated (if neccessary) food trail.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      The newly updated dictionary showing the positions of the ants. 
      Keys are ant IDs as strings.
      Values are None, int or "anthill" (string).
    
    anthill : (list)
      The newly updated (if neccessary) anthill list.
      Elements are None or ant IDs as strings.

    anthill_food_tokens : (dict)
      The newly updated (if necessary) collection of food tokens stored by the anthill.
      Keys are food IDs as strings.
      Values are integers >= 0
    """
    ant = self.choose_ant(ant_positions, PROMPT_TEXT_GAME_CHOICE_ANT)

    if self.goes_to_anthill(ant, trail, ant_positions):
      return self.go_to_anthill(trail, ant_positions, anthill, anthill_rule, ant, anthill_food_tokens)
    else:
      ant_positions = self.move_ant_along_trail(trail, ant_positions, ant)
      allowed_choices_direction = self.define_allowed_choices_direction(ant, trail, ant_positions)
      direction = self.make_choice(allowed_choices_direction, PROMPT_TEXT_GAME_CHOICE_DIRECTION)
      (food_to_hand, trail) = self.take_food_from_trail(trail, ant_positions, ant, direction)
      self.store_food(food_to_hand)

    return (trail, ant_positions, anthill, anthill_food_tokens)

  def goes_to_anthill(self, ant, trail, ant_positions):
    """Defines whether the chosen ant will move onto the anthill or not.

    Parameters
    ----------
    ant : (string)
      The ID of the ant which has been chosen to be moved.

    trail : (list)
      The trail contains a list of the food tokens available on the game area.
      The types of food token can be found in constants.py/FOOD_TYPES.
      As food tokens are removed from the game the elements are replaced with None.

    ant_positions : (dict)
      A dictionary showing the starting location of each ant.
      The position on the trail will be defined as the index of the 
      element in the trail list.
      Keys are strings.
      Values are ant position as None or int or "anthill".

    Returns
    -------
    (boolean)
      True if the chosen ant's next (current) move will result in it being placed on the anthill.
      False if the chosen ant's next (current) move will result in it being moved along the trail.
    """
    if ant_positions[ant] == None:
      trail_to_check = trail
    else:
      trail_to_check = trail[ant_positions[ant]+1:]

    if K_COLOUR_V_FOOD_DICT[ant] not in trail_to_check:
      return True
    else:
      return False

  def define_allowed_choices_anthill_food(self, anthill_food_tokens):
    """Provides the list of permitted food-picking options to the player.

    Determines which food tokens are available to collect when 
    placing an ant on the anthill.
    Any food token that is present in the anthill food tokens is available for collection.
    
    Parameters
    ----------
    anthill_food_tokens : (dict)
      The remaining food tokens at the anthill which the players will choose from.
      Keys are food IDs as strings.
      Values are integers >= 0.

    Returns
    -------
    allowed_choices_anthill_food : (list)
      All of the keys from anthill_food_tokens whose values are >= 1.
      Elements are food IDs as strings.
    """
    allowed_choices_anthill_food = [k for k, v in anthill_food_tokens.items() if v >= 1]
    return allowed_choices_anthill_food

  def take_food_from_anthill(self, anthill_food_tokens, user_choice_food):
    """Remove the player's chosen food token from the anthill supply.

    Parameters
    ----------
    anthill_food_tokens : (dict)
      The remaining food tokens at the anthill which the players will choose from.
      Keys are food IDs as strings.
      Values are integers >= 0.

    user_choice_food : (string)
      The ID of the choice the player has made.
      In this case, a food type.
    """
    anthill_food_tokens[user_choice_food] -= 1
    return anthill_food_tokens

  def define_allowed_choices_anthill_placement(self, anthill):
    """Provides the list of permitted anthill-level-picking options to the player.

    Determines which anthill levels are vacant and can have an ant placet there. 
    For use in games with 'user choice' anthill rule.

    Parameters
    ----------
    anthill : (list)
      A list showing the current state of the game's anthill.
      Initialised with each element as None.
      Elements will be changed into the IDs of the ants as they reach the anthill.
      Each element is None or string.

    Returns
    -------
    allowed_choices_placement : (list)
      A list containing the indices of any/all vacant locations in the anthill.
      The indices are converted to strings to ensure compatibility with make_choice().
    """
    allowed_choices_placement = []
    for idx, level in enumerate(anthill):
      if level is None:
        allowed_choices_placement.append(str(idx))
    return allowed_choices_placement

  def score_hand(self, anthill, standard_tokens_for_trail, wine_rule):
    """Calculates the player's total points at the end of the game.

    Could be called any time but to reflect the real game there is no running 
    total of points; just a single calculation and comparison after the final ant 
    has reached the anthill.

    Adds together the standard_food_score and the wine_score.

    Updates
    -------
    score : (integer)
      The player's total points for this game. 
      Will be initialised at 0
      Will be updated at the end of the game.
    """
    wine_score = self.score_wine(standard_tokens_for_trail, wine_rule)
    standard_score = self.score_standard_food_in_hand(anthill) 
    self.score = standard_score + wine_score

  def score_wine(self, standard_tokens_for_trail, wine_rule):
    """Calculates the player's 'wine' points at the end of the game. 

    'Wine' points are those points that are earned through the possession of wine 
    tokens in combination with this game's specific wine-rule. 

    Wine rules are set at the time the game is started and whichever one is used, 
    the correct method is called here.

    Parameters
    ----------
    standard_tokens_for_trail : (dict)
      A dictionary containing the 'standard' tokens used to prepare the trail for this game. 

      Used to cross-reference the player's hand to see which tokens will 
      interact with the wine.
      Keys are food types as strings
      Values are integers.

    wine_rule : (string)
      The wine rule which was chosen during game set-up.

    Returns
    -------
    wine_score : (integer)
      An integer showing the player's total points from wine. 
    """
    wine_score = 0
    if "wine" in self.hand:
      wine_scoring_function = WINE_CARD_DICT[wine_rule]
      wine_score = wine_scoring_function(self.hand, standard_tokens_for_trail)
    return wine_score

  def spend_chocolate(self):
    """Removes one chocolate token from player's hand.

    Reduces chocolate by 1, or removes completely from hand if only one is present.
    Will return unchanged hand if hand already has no chocolate.
    """
    if "chocolate" in self.hand:
      if self.hand["chocolate"] == 1:
        self.hand.pop("chocolate")
      else:
        self.hand["chocolate"] -= 1
    
  def ask_to_spend_chocolate(self):
    """Checks if the player would like to spend a chocolate token.

    Prompts the player to enter 'yes' or 'no' depending on if they would like to 
    spend a chocolate.

    Returns
    -------
    (boolean)
      True if the player chooses to spend a chocolate.
      False if the player chooses not to spend a chocolate.
    """
    print("\nPlease enter 'yes' or 'no'.")
    user_choice = input("%s; would you like to spend a chocolate token?\n" % self.name)
    if user_choice == "no":
      return False
    elif user_choice == "yes":
      return True
    else:
      return self.ask_to_spend_chocolate()

  def will_spend_choc(self):
    """Checks if the player is going to spend chocolate this turn. 

    Verifies if player is able and willing to spend a chocolate token this turn.

    Returns
    -------
    (boolean)
      False if no chocolate in player's hand
      False if chocolate in player's hand but player opts not to spend chocolate
      True if chocolate in player's hand and player does opt to spend chocolate.
    """
    if "chocolate" in self.hand:
      return self.ask_to_spend_chocolate()
    else:
      return False

  def take_turbo_turn(self, trail, ant_positions, anthill, anthill_rule, anthill_food_tokens):
    """Performs actions for player to carry out the 'Turbo' special chocolate action.

    Makes up to two moves along the trail; or moves ant to anthill after one or two moves 
    if appropriate. At the end of the move(s) the player will pick a food from the trail 
    or from the anthill and add this to their hand.

    Parameters
    ----------
    trail : (list)
      The shuffled list of all the food tiles being used in the game.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      Dictionary containing the current locations of each ant.
      Keys are ants as strings.
      Values are ant positions as None, int or "anthill" (string).

    anthill : (list)
      List of equivalent length as the number of ants in the game. 
      Shows which (if any) ants have moved past the end of the trail and their positions on the anthill.
      Elements are None or ant IDs as strings.

    anthill_rule : (list)
      A list defining the order in which the anthill should be filled as ants arrive 
      throughout the game. 

    anthill_food_tokens : (dict)
      Contains the record of which and how many of each food token are stored at the anthill.
      Keys are food types as strings.
      Values are integers >=0

    Returns
    -------
    trail : (list)
      The newly updated (if neccessary) food trail.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      The newly updated dictionary showing the positions of the ants. 
      Keys are ant IDs as strings.
      Values are None, int or "anthill" (string).
    
    anthill : (list)
      The newly updated (if neccessary) anthill list.
      Elements are None or ant IDs as strings.

    anthill_food_tokens : (dict)
      The newly updated (if necessary) collection of food tokens stored by the anthill.
      Keys are food IDs as strings.
      Values are integers >= 0.
    """
    ant = self.choose_ant(ant_positions, PROMPT_TEXT_GAME_CHOICE_ANT)

    if self.goes_to_anthill(ant, trail, ant_positions):
      return self.go_to_anthill(trail, ant_positions, anthill, anthill_rule, ant, anthill_food_tokens)
    else:
      ant_positions = self.move_ant_along_trail(trail, ant_positions, ant)
      if self.goes_to_anthill(ant, trail, ant_positions):
        return self.go_to_anthill(trail, ant_positions, anthill, anthill_rule, ant, anthill_food_tokens)
      else:
        ant_positions = self.move_ant_along_trail(trail, ant_positions, ant)
        allowed_choices_direction = self.define_allowed_choices_direction(ant, trail, ant_positions)
        direction = self.make_choice(allowed_choices_direction, PROMPT_TEXT_GAME_CHOICE_DIRECTION)
        (food_to_hand, trail) = self.take_food_from_trail(trail, ant_positions, ant, direction)
        self.store_food(food_to_hand)

    return (trail, ant_positions, anthill, anthill_food_tokens)

  def take_turn(self, trail, ant_positions, anthill, anthill_rule, anthill_food_tokens, chocolate_rule):
    """Checks if player is taking a standard turn or using the special chocolate action.

    Calls the appropriate methods to check if player is able & willing to use a chocolate 
    token this turn; reduce the number of choclate tokens in the player's hand if necessary; 
    then perform the actions corresponding to a standard turn or a special chocolate turn 
    accordingly.

    Parameters
    ----------
    trail : (list)
      The shuffled list of all the food tiles being used in the game.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      Dictionary containing the current locations of each ant.
      Keys are ants as strings.
      Values are ant positions as None, int or "anthill" (string).

    anthill : (list)
      List of equivalent length as the number of ants in the game. 
      Shows which (if any) ants have moved past the end of the trail and their positions on the anthill.
      Elements are None or ant IDs as strings.

    anthill_rule : (list)
      A list defining the order in which the anthill should be filled as ants arrive 
      throughout the game. 

    anthill_food_tokens : (dict)
      Contains the record of which and how many of each food token are stored at the anthill.
      Keys are food types as strings.
      Values are integers >=0.

    Returns
    -------
    trail : (list)
      The newly updated (if neccessary) food trail.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      The newly updated dictionary showing the positions of the ants. 
      Keys are ant IDs as strings.
      Values are None, int or "anthill" (string).
    
    anthill : (list)
      The newly updated (if neccessary) anthill list.
      Elements are None or ant IDs as strings.

    anthill_food_tokens : (dict)
      The newly updated (if necessary) collection of food tokens stored by the anthill.
      Keys are food IDs as strings.
      Values are integers >= 0.
    """
    if self.will_spend_choc():
      self.spend_chocolate()
      chocolate_method = getattr(self, CHOCOLATE_CARD_DICT[chocolate_rule])
      (trail, ant_positions, anthill, anthill_food_tokens) = \
        chocolate_method(trail, ant_positions, anthill, anthill_rule, anthill_food_tokens)
    else:
      (trail, ant_positions, anthill, anthill_food_tokens) = \
        self.take_standard_turn(trail, ant_positions, anthill, anthill_rule, anthill_food_tokens)
    
    return (trail, ant_positions, anthill, anthill_food_tokens)

  def take_doubler_turn(self, trail, ant_positions, anthill, anthill_rule, anthill_food_tokens):
    """Performs actions for player to carry out the 'Doubler' special chocolate action.

    Makes one move either along the trail or onto anthill as appropriate. If move ends 
    on anthill; player chooses one food and adds this to their hand; if move ends on the 
    trail; player chooses food twice and adds both to their hand.

    Parameters
    ----------
    trail : (list)
      The shuffled list of all the food tiles being used in the game.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      Dictionary containing the current locations of each ant.
      Keys are ants as strings.
      Values are ant positions as None, int or "anthill" (string).

    anthill : (list)
      List of equivalent length as the number of ants in the game. 
      Shows which (if any) ants have moved past the end of the trail and their positions on the anthill.
      Elements are None or ant IDs as strings.

    anthill_rule : (list)
      A list defining the order in which the anthill should be filled as ants arrive 
      throughout the game. 

    anthill_food_tokens : (dict)
      Contains the record of which and how many of each food token are stored at the anthill.
      Keys are food types as strings.
      Values are integers >=0.

    Returns
    -------
    trail : (list)
      The newly updated (if neccessary) food trail.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      The newly updated dictionary showing the positions of the ants. 
      Keys are ant IDs as strings.
      Values are None, int or "anthill" (string).
    
    anthill : (list)
      The newly updated (if neccessary) anthill list.
      Elements are None or ant IDs as strings.

    anthill_food_tokens : (dict)
      The newly updated (if necessary) collection of food tokens stored by the anthill.
      Keys are food IDs as strings.
      Values are integers >= 0.
    """
    ant = self.choose_ant(ant_positions, PROMPT_TEXT_GAME_CHOICE_ANT)
    
    if self.goes_to_anthill(ant, trail, ant_positions):
      return self.go_to_anthill(trail, ant_positions, anthill, anthill_rule, ant, anthill_food_tokens)
    else:
      ant_positions = self.move_ant_along_trail(trail, ant_positions, ant)
      for i in range(2):
        allowed_choices_direction = self.define_allowed_choices_direction(ant, trail, ant_positions)
        direction = self.make_choice(allowed_choices_direction, PROMPT_TEXT_GAME_CHOICE_DIRECTION)
        (food_to_hand, trail) = self.take_food_from_trail(trail, ant_positions, ant, direction)
        self.store_food(food_to_hand)

    return (trail, ant_positions, anthill, anthill_food_tokens)

  def go_to_anthill(self, trail, ant_positions, anthill, anthill_rule, ant, anthill_food_tokens):
    """Performs actions for an ant to move onto the anthill.

    Parameters
    ----------
    trail : (list)
      The shuffled list of all the food tiles being used in the game.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      Dictionary containing the current locations of each ant.
      Keys are ants as strings.
      Values are ant positions as None, int or "anthill" (string).

    anthill : (list)
      List of equivalent length as the number of ants in the game. 
      Shows which (if any) ants have moved past the end of the trail and their positions on the anthill.
      Elements are None or ant IDs as strings.

    anthill_rule : (list)
      A list defining the order in which the anthill should be filled as ants arrive 
      throughout the game. 

    anthill_food_tokens : (dict)
      Contains the record of which and how many of each food token are stored at the anthill.
      Keys are food types as strings.
      Values are integers >=0.

    Returns
    -------
    trail : (list)
      The newly updated (if neccessary) food trail.
      Elements are food types as strings or None.
    
    ant_positions : (dict)
      The newly updated dictionary showing the positions of the ants. 
      Keys are ant IDs as strings.
      Values are None, int or "anthill" (string).
    
    anthill : (list)
      The newly updated (if neccessary) anthill list.
      Elements are None or ant IDs as strings.

    anthill_food_tokens : (dict)
      The newly updated (if necessary) collection of food tokens stored by the anthill.
      Keys are food IDs as strings.
      Values are integers >= 0
    """
    (anthill, ant_positions) = self.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant)
    allowed_choices_anthill_food = self.define_allowed_choices_anthill_food(anthill_food_tokens)
    user_choice_food = self.make_choice(allowed_choices_anthill_food, PROMPT_TEXT_GAME_CHOICE_FOOD) 
    anthill_food_tokens = self.take_food_from_anthill(anthill_food_tokens, user_choice_food)
    self.store_food(user_choice_food)

    return (trail, ant_positions, anthill, anthill_food_tokens)

  def choose_ant(self, ant_positions, prompt_text):
    """Performs the actions for a player to select which ant they will move this turn.

    Parameters
    ----------
    ant_positions : (dict)
      Dictionary containing the current locations of each ant.
      Keys are ants as strings.
      Values are ant positions as None, int or "anthill" (string).

    prompt_text : (string)
      A sentence which will prompt the player to make the appropriate choice.

    Returns
    -------
    ant : (string)
      The ID of the ant which has been chosen to be moved.
    """
    allowed_choices_ants = self.define_allowed_choices_ants(ant_positions)
    ant = self.make_choice(allowed_choices_ants, prompt_text)
    return ant
