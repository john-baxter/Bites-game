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
    self.ant_positions = self.initialise_ant_positions(ants)
    self.trail = self.initialise_trail(tokens_for_trail)
    self.anthill = self.initialise_anthill(ants)
    self.players = players

  def initialise_ant_positions(self, ants):
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

  def take_all_turns(self):
    """Cycles through all players and performs actions needed to take their turns.

    Continues to cycle through players repeatedly until the end of the game.
    The end of the game is recognised as the point where all ants are on the anthill.
    The loop is broken immediately as this criterion is met.
    """
    self.render_game()
    while 1:
      for player in self.players:
        (self.trail, self.ant_positions, self.anthill) = \
          player.take_turn(
            self.trail, self.ant_positions, self.anthill)
        self.render_game()
        if None not in self.anthill: return

  def calculate_and_print_scores(self):
    """Displays each player's score

    Prints each player's name and shows how many points they have.
    """
    for player in self.players:
      player.score_hand(self.anthill)     
      print ("%s: %i\n" % (player.name, player.score))

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
    self.print_players_names_and_hands()
    self.print_ants_positioned_before_the_trail()
    self.print_trail_and_ants_positioned_thereon()
    self.print_ants_positioned_on_anthill_top_down()
    
  def print_players_names_and_hands(self):
    """Shows the names of each player and what (if any) food tokens thay have in their hand.
    """
    print("\nPlayer names and hands:")
    for player in self.players:
      print("%s: %s" % (player.name, player.hand))

  def print_ants_positioned_before_the_trail(self):
    """Shows which ants (if any) are positioned at the start, before the trail
    """
    if len([e for e in self.ant_positions.values() if e is None]) > 0:
      print("\nAnts at the beginning of the trail:")
      for k, v in self.ant_positions.items():
        if v is None:
          print(k)

  def print_trail_and_ants_positioned_thereon(self):
    """Shows the list of food tokens or None elements in the trail.

    Also shows the positions of any ants positioned on the trail
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
      else:
        print(food)

  def print_ants_positioned_on_anthill_top_down(self):
    """Shows a representation of the anthill as text
    """
    print("\nAnthill:")
    for i in range(len(self.anthill)-1, -1, -1):
      if self.anthill[i] is None:
        print("Level %s is empty" % i)
      else:
        print("The %s ant is in level %s" % (self.anthill[i], i))
    
if __name__ == '__main__':
  from player import Player
  from constants import ANTS, TOKENS_FOR_TRAIL
  ana = Player("Ana")
  john = Player("John")
  rafa = Player("Rafa")
  peter = Player("Peter")
  players = [ana, john]
  # players = [john, peter]
  bites_game = Bites(ANTS, TOKENS_FOR_TRAIL, players)
  bites_game.play_full_game()
