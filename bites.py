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

  def print_scores(self):
    """Displays each player's score

    Prints each player's name and shows how many points they have.
    """
    for player in self.players:
      print ("%s: %i\n" % (player.name, player.score))

  def play_full_game(self):
    """Runs through a full game

    Takes all player turns as necessary and prints player scores.
    """
    self.take_all_turns()
    self.print_scores()

  def render_game(self):
    self.print_players_names_and_hands()
    self.print_ants_positioned_before_the_trail()
    self.print_trail_and_ants_positioned_thereon()
    
    # print("\nAnthill: %s\n" % self.anthill)

  def print_players_names_and_hands(self):
    for player in self.players:
      print("%s: %s" % (player.name, player.hand))

  def print_ants_positioned_before_the_trail(self):
    for k, v in self.ant_positions.items():
      if v is None:
        print(k)

  def print_trail_and_ants_positioned_thereon(self):
    reverse_ant_positions = dict((v, k) for k, v in self.ant_positions.items())
    for i, food in enumerate(self.trail):
      if i in reverse_ant_positions:
    #     # TODO: instead of 6, use the length of the longest food, 
    #     # which is 6, but in case different foods are used another time.
        print("%s %s" % (food, reverse_ant_positions[i]))
        # print("%s %s" % (food.ljust(6), reverse_ant_positions[i]))
      else:
        print(food)
    

if __name__ == '__main__':
  from player import Player
  from constants import ANTS, TOKENS_FOR_TRAIL
  ana = Player("Ana")
  john = Player("John")
  players = [ana, john]
  bites_game = Bites(ANTS, TOKENS_FOR_TRAIL, players)
  # bites_game.players[0].hand = {"cheese": 1, "grapes": 1}
  # bites_game.anthill = [None, None, None, None, "red"]
  # bites_game.ant_positions = {"yellow": 5, "purple": 7, "green": None}
  # bites_game.render_game()
  bites_game.play_full_game()