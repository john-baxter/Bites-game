from constants import MIN_PLAYERS, MAX_PLAYERS
from constants import ANTS, TOKENS_FOR_TRAIL
from constants import ANTHILL_CARD_DICT
from player import Player
from bites import Bites
from random import randint
from functions import show_allowed_choices_from_list

def enter_number_of_players():
  """Sets the number of players for the game

  Prompts the user to input the number of players that will be playing the game. 
  Verifies that the user input is:
    - a number.
    - in the correct range.

  Returns
  -------
  number_of_players : (int)
    The number of players that will be playing this game.
  """
  while 1:
    number_of_players = input("Please enter the number of players: ")
    try:
      number_of_players = int(number_of_players)
      if number_of_players in range(MIN_PLAYERS, MAX_PLAYERS+1):
        return number_of_players
    except ValueError:
      print("Please enter an integer") 

def generate_player():
  """Creates an instance of the Player class.

  Prompts the user to enter the name of a player and uses that input as the Player.name 
  attribute while instantiating a Player object.

  Returns
  -------
  player : (Player)
    A Player object with the given input as the .name attribute.
  """
  name = input("Please enter your name: ")
  player = Player(name)
  return player

def prepare_list_of_players():
  """Creates a list of Player objects.

  Instantiates the correct number of players based on the given number of players, and 
  sets the name attribute for each one. Adds each one in turn to a list of players.
  
  Returns
  -------
  players : (list)
    A list of all the players that will be playing this game. 
    Each element is an instance of the Player class.
  """
  players = []
  number_of_players = enter_number_of_players()
  while len(players) < number_of_players:
    players.append(generate_player())
  return players

def start_new_game():
  """Instantiates the Bites class with appropriate arguments and starts a new game.

  Gathers together all the required information, generates an instance of the 
  Bites class and calls the Bites method that will trigger the start 
  (and continuation) of a game of Bites.
  """
  players = prepare_list_of_players()
  anthill_order = choose_anthill_rule()
  play_bites = Bites(ANTS, TOKENS_FOR_TRAIL, players, anthill_order)
  play_bites.play_full_game()

def choose_anthill_rule(anthill_card_dict=None):
  """Allows the user to choose the anthill rule for this game

  Select one of the available options or allow the game to select one at random.

  Parameters
  ----------
  anthill_card_dict : (dict)
    A dictionary containing the available options of anthill rule choice.
    Referred to as 'cards' to reflect the real Bites game.
    Keys are names of rules as strings
    Values are the implementation of those rules as lists.

  Returns
  -------
  card_choice : (string)
    The string value from the keys of anthill_card_dict that has been selected
  """
  if anthill_card_dict is None:
    anthill_card_dict=ANTHILL_CARD_DICT
  anthill_card_allowed_choices = list(anthill_card_dict.keys())
  show_allowed_choices_from_list(anthill_card_allowed_choices)
  print("Or enter 'random' to select one of the above options")
  card_choice = input("Please enter your choice of anthill card: ")

  if card_choice in anthill_card_allowed_choices:
    return card_choice
  elif card_choice == "random":
    return anthill_card_allowed_choices[randint(0, len(anthill_card_allowed_choices)-1)]
  else:
    return choose_anthill_rule()

if __name__ == '__main__':
  start_new_game()
