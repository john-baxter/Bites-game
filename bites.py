import random
from constants import K_COLOUR_V_FOOD_DICT, STANDARD_TOKENS_FOR_TRAIL
from constants import ANTHILL_CARD_DICT

class Bites():
  def __init__(self, ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule):
    """Initialises an instance of the Bites class.

    This is the equivalent of setting up the game on the table ready to start playing.

    Parameters
    ----------
    ants : (list)
      The list of the ants which will be used for the game. 
      Each element is a string.

    standard_tokens_for_trail : (dict)
      The names of each type of standard food token and their quantities
      The keys are names of food as strings.
      The values are the amount of the food as integers.
    
    wine_tokens_for_trail : (dict)
      A single key-value pair showing the number of wine tokens used in the trail for this game
      The key is 'wine'.
      The value is an integer.

    chocolate_tokens_for_trail : (dict)
      A single key-value pair showing the number of chocolate tokens used 
      in the trail for this game
      The key is 'chocolate'.
      The value is an integer.

    players : (list)
      A list of Player objects representing the players of this game.
      Elements are instances of the Player class
    
    anthill_rule : (string)
      The identity of the anthill rule that has been chosen during the setup of the game.

    wine_rule : (string)
      The identity of the wine rule that has been chosen during the setup of the game.

    chocolate_rule : (string)
      The identity of the chocolate rule that has been chosen during the setup of the game.

    Attributes
    ----------
    ant_positions : (dict)
      The current position of each ant
      Initialised with each position as None and will be updated through the 
      game refering to the index of the trail list element the ant is positioned at.
      Keys are ant IDs as strings
      Values are integers or None

    standard_tokens_for_trail : (dict)
      The names of each type of standard food token and their quantities
      The keys are names of food as strings.
      The values are the amount of the food as integers.
    
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

    anthill_food_tokens : (dict)
      One of each type of food token.
      Keys are foods as strings
      Values are integers initialised as 1

    anthill_rule : (string)
      The identity of the anthill rule that has been chosen during the setup of the game.

    wine_rule : (string)
      The identity of the wine rule that has been chosen during the setup of the game.
    
    chocolate_rule : (string)
      The identity of the chocolate rule that has been chosen during the setup of the game.
    """
    self.ant_positions = self.initialise_ant_positions(ants)
    self.standard_tokens_for_trail = standard_tokens_for_trail
    self.trail = self.initialise_trail(wine_tokens_for_trail, chocolate_tokens_for_trail)
    self.anthill = self.initialise_anthill(ants)
    self.players = players
    self.anthill_food_tokens = self.initialise_anthill_food_tokens()
    self.anthill_rule = anthill_rule
    self.wine_rule = wine_rule
    self.chocolate_rule = chocolate_rule

  def initialise_ant_positions(self, ants):
    """Create a record of the starting positions of each insect meeple.
    
    This will show the starting positions as None, since the ants are not 
    positioned on the trail immediately.

    Parameters
    ----------
    ants : (list)
      A list containing the ID of each ant, referred to by colour
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
    """Create the ending position for the insect meeple ready for the end of the path.

    Parameters
    ----------
    ants : (list)
      A list containing the ID of each ant, referred to by colour
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
  
  def create_partial_trail_of_standard_and_wine(self, wine_tokens_for_trail):
    """Create the path of tokens that the game is played on.

    Uses the attribute standard_tokens_for_trail and the passed wine_tokens_for_trail 
    and shuffles these together.
    
    Parameters
    ----------
    wine_tokens_for_trail : (dict)
      The wine tokens used for this trail.
      Key is "wine"
      Value is int
    
    Returns
    -------
    trail : (list)
      A random shuffled list of all the tokens given in the tokens_for_trail argument
      Each element is a string.
    """
    partial_trail = []
    for food, amount in dict(self.standard_tokens_for_trail, ** wine_tokens_for_trail).items():
      partial_trail = partial_trail + ([food] * amount)
    random.shuffle(partial_trail)
    return partial_trail

  def take_all_turns(self):
    """Cycles through all players and performs actions needed to take their turns.

    Continues to cycle through players repeatedly until the end of the game.
    The end of the game is recognised as the point where all ants are on the anthill.
    The loop is broken immediately as this criterion is met.
    """
    self.render_game()
    while 1:
      for player in self.players:
        (self.trail, self.ant_positions, self.anthill, self.anthill_food_tokens) = \
          player.take_turn(
            self.trail, self.ant_positions, self.anthill, self.anthill_rule, self.anthill_food_tokens, self.chocolate_rule)
        self.render_game()
        if None not in self.anthill: return

  def calculate_and_print_scores(self):
    """Displays each player's score

    Prints each player's name and shows how many points they have.
    """
    print("\nThe results: ")
    for player in self.players:
      player.score_hand(self.anthill, self.standard_tokens_for_trail, self.wine_rule)     
      print ("%s: %i" % (player.name, player.score))

  def play_full_game(self):
    """Runs through a full game

    Takes all player turns as necessary and prints player scores.
    """
    self.take_all_turns()
    self.calculate_and_print_scores()

  def render_game(self):
    """Shows the various elements of the game on the screen.

    Calls other methods, each of which shows a section of the game setup.
    """
    self.print_wine_rule_statement()
    self.print_chocolate_rule_statement()
    self.print_players_names_and_hands()
    self.print_ants_positioned_before_the_trail()
    self.print_trail_and_ants_positioned_thereon()
    self.print_ants_positioned_on_anthill_top_down()
    self.print_anthill_food_tokens()
    
  def print_players_names_and_hands(self):
    """Shows the names of each player and what (if any) food tokens thay have in their hand.
    """
    print("\nPlayer names and hands:")
    for player in self.players:
      print("%s: %s" % (player.name, player.hand))

  def print_ants_positioned_before_the_trail(self):
    """Shows which ants (if any) are positioned at the start, before the trail.
    """
    if len([e for e in self.ant_positions.values() if e is None]) > 0:
      print("\nAnts at the beginning of the trail:")
      for k, v in self.ant_positions.items():
        if v is None:
          print(k)

  def print_trail_and_ants_positioned_thereon(self):
    """Shows the list of food tokens or None elements in the trail.

    None elements are replaced by '--'.
    Also shows the positions of any ants positioned on the trail.
    """
    if len([e for e in self.ant_positions.values() if isinstance(e, int)]) > 0:
      print("\nTrail and ant positions:")
    else:
      print("\nTrail:")
    
    reverse_ant_positions = dict((v, k) for k, v in self.ant_positions.items())
    just = len(max(self.ant_positions.keys(), key=len))
    for i, food in enumerate(self.trail):
      if i in reverse_ant_positions:
        print("%s %s" % (food.ljust(just), reverse_ant_positions[i]))
      elif food is None:
        print("--")
      else:
        print(food)

  def print_ants_positioned_on_anthill_top_down(self):
    """Shows a representation of the anthill as text.
    """
    print("\nAnthill:")
    print("Ants will be placed on the anthill according to the rule: %s" % self.anthill_rule)
    for i in range(len(self.anthill)-1, -1, -1):
      if self.anthill[i] is None:
        print("Level %s is empty" % i)
      else:
        print("The %s ant is in level %s" % (self.anthill[i], i))

  def initialise_anthill_food_tokens(self):
    """Prepare the stack of tokens next to the anthill.

    The stack has one of each standard food. Does not include special food.
    Players get to collect one each time they place an ant on the anthill.

    Returns
    -------
    anthill_food_tokens : (dict)
      One of each type of standard food token.
      Keys are foods as strings
      Values are integers initialised as 1
    """
    self.anthill_food_tokens = { token : 1 for token in self.standard_tokens_for_trail }
    return self.anthill_food_tokens

  def print_anthill_food_tokens(self):
    """Shows the collection of food tokens currently positioned at the anthill
    """
    if sum(list(self.anthill_food_tokens.values())) > 0:
      print("\nAnthill food tokens")
      list_of_anthill_food_tokens = []
      for k, v in self.anthill_food_tokens.items():
        for n in range(v):
          list_of_anthill_food_tokens.append(k)
      print(list_of_anthill_food_tokens)

  def print_wine_rule_statement(self):
    """Shows text informing the players which wine rule is in play for this game.
    """
    print("\nThe wine scoring card currently in play is: ")
    print("%s" % self.wine_rule.capitalize())

  def identify_chocolate_limit(self, partial_trail):
    """Find the lower limit of where chocolate could be placed into the trail. 

    Chocolate tokens must not be available on the first turn of the game so must only be 
    inserted into the trail (at random) starting from the position of the last unique 
    standard food +2.

    Parameters
    ----------
    partial_trail : (list)
      A list of tokens that will be used as part of the trail for this game. 
      Elements are standard food tokens and wine as strings.

    Returns
    -------
    chocolate_limit : (int)
      The index within the partial trail that is the first position chocolate is 
      allowed to be placed.
    """
    chocolate_limit = max([partial_trail.index(food) for food in self.standard_tokens_for_trail]) + 2
    return chocolate_limit

  def add_chocolate_into_trail(self, partial_trail, chocolate_tokens_for_trail):
    """Adds chocolate tokens into the trail as appropriate

    Shuffles the given number of chocolate tokens into the slice of the trail 
    after the chocolate limit.

    Parameters
    ----------
    partial_trail : (list)
      A shuffled list of tokens other than chocolate that will be used for this game.
      Elements are standard food or wine tokens as strings
    
    chocolate_tokens_for_trail : (dict)
      A dictionary containing the chocolate tokens that will be used for this game.
      Key is 'chocolate' as string
      Value is int

    Returns
    -------
    trail : (list)
      A shuffled list of all tokens that will be used for this game. 
      The slice pre-chocolate_lim is unchanged.
      The slice post-chocolate_limit has had chocolate added and been reshuffled.
      Elements are standard, wine and chocolate tokens as strings.
    """
    trail = partial_trail 
    chocolate_limit = self.identify_chocolate_limit(partial_trail)
    for food, amount in chocolate_tokens_for_trail.items():
      trail += [food] * amount
    trail_pre_choc_slice = trail[:chocolate_limit]
    trail_with_choc_slice = trail[chocolate_limit:]
    random.shuffle(trail_with_choc_slice)
    trail = trail_pre_choc_slice + trail_with_choc_slice
    return trail

  def initialise_trail(self, wine_tokens_for_trail, chocolate_tokens_for_trail):
    """Creates the trail of food tokens that this game will be played on.

    Adds together the standard tokens and the wine, shuffles, appends the 
    chocolate and shuffles these into the appropriate slice.

    Parameters
    ----------
    wine_tokens_for_trail : (dict)
      A single key-value pair showing the number of wine tokens used in the trail for this game.
      The key is 'wine'.
      The value is an integer.
      
    chocolate_tokens_for_trail : (dict)
      A single key-value pair showing the number of chocolate tokens used
      in the trail for this game.
      The key is 'chocolate'.
      The value is an integer.

    Returns
    -------
    trail : (list)
      The shuffled (with appropriate restriction) list of all tokens used for this game.
    """
    partial_trail = self.create_partial_trail_of_standard_and_wine(wine_tokens_for_trail)
    trail = self.add_chocolate_into_trail(partial_trail, chocolate_tokens_for_trail)
    return trail

  def print_chocolate_rule_statement(self):
    """Shows text informing the players which chocolate rule is in play for this game.
    """
    print("\nThe chocolate action card currently in play is: ")
    print("%s" % self.chocolate_rule.capitalize())
