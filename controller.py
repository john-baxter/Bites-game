from constants import MIN_PLAYERS, MAX_PLAYERS
from constants import ANTS, STANDARD_TOKENS_FOR_TRAIL, WINE_TOKENS_FOR_TRAIL, CHOCOLATE_TOKENS_FOR_TRAIL
from constants import ANTHILL_CARD_DICT, PROMPT_TEXT_RULE_CHOICE_ANTHILL
from constants import WINE_CARD_DICT, PROMPT_TEXT_RULE_CHOICE_WINE
from constants import CHOCOLATE_CARD_DICT, PROMPT_TEXT_RULE_CHOICE_CHOCOLATE
from player import Player
from bites import Bites
from random import randint
from functions import show_allowed_choices_from_list

def enter_number_of_players():
  """Sets the number of players for the game.

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
  anthill_rule = choose_game_rule(ANTHILL_CARD_DICT, PROMPT_TEXT_RULE_CHOICE_ANTHILL)
  wine_rule = choose_game_rule(WINE_CARD_DICT, PROMPT_TEXT_RULE_CHOICE_WINE)
  chocolate_rule = choose_game_rule(CHOCOLATE_CARD_DICT, PROMPT_TEXT_RULE_CHOICE_CHOCOLATE)
  play_bites = Bites(
    ANTS, 
    STANDARD_TOKENS_FOR_TRAIL, 
    WINE_TOKENS_FOR_TRAIL, 
    CHOCOLATE_TOKENS_FOR_TRAIL, 
    players, 
    anthill_rule, 
    wine_rule, 
    chocolate_rule,
    )
  play_bites.play_full_game()

def choose_game_rule(rule_card_dict, prompt_text):
  """Allows the user to choose a rule for this game

  Select one of the available options or allow the game to select one at random.

  Parameters
  ----------
  rule_card_dict : (dict)
    A dictionary containing the available options of rule choice.
    Referred to as 'cards' to reflect the real Bites game.
    Keys are names of rules as strings
    Values are the implementation of those rules in various forms including:
      - list
      - method object
      - method name as string
      - None

  Returns
  -------
  card_choice : (string)
    The string value from the keys of rule_card_dict that has been selected.
  """
  rule_card_allowed_choices = list(rule_card_dict.keys())
  show_allowed_choices_from_list(rule_card_allowed_choices)
  print("Or enter 'random' to select one of the above options")
  card_choice = input(prompt_text)

  if card_choice in rule_card_allowed_choices:
    return card_choice
  elif card_choice == "random":
    return rule_card_allowed_choices[randint(0, len(rule_card_allowed_choices)-1)]
  else:
    return choose_game_rule(rule_card_dict, prompt_text)

if __name__ == '__main__':
  start_new_game()
