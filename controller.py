from constants import MIN_PLAYERS, MAX_PLAYERS
from constants import ANTS, TOKENS_FOR_TRAIL
from constants import ANTHILL_ORDER_TOP_DOWN, ANTHILL_ORDER_BOTTOM_UP
from player import Player
from bites import Bites

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
  play_bites = Bites(ANTS, TOKENS_FOR_TRAIL, players)
  play_bites.play_full_game()

def choose_anthill_rule():
  card_choice = input()
  if card_choice == "bottom up":
    return ANTHILL_ORDER_BOTTOM_UP
  
  return ANTHILL_ORDER_TOP_DOWN

if __name__ == '__main__':
  start_new_game()
