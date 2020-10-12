from constants import MIN_PLAYERS, MAX_PLAYERS
from constants import ANTS, TOKENS_FOR_TRAIL
from player import Player
from bites import Bites

def enter_number_of_players():
  number_of_players = 0
  while number_of_players not in range(MIN_PLAYERS, MAX_PLAYERS+1):
    number_of_players = int(input("Please enter the number of players: "))
  return number_of_players

def generate_player():
  name = input("Please enter your name: ")
  player = Player(name)
  return player

def prepare_list_of_players():
  players = []
  number_of_players = enter_number_of_players()
  while len(players) < number_of_players:
    players.append(generate_player())
  return players

def start_new_game():
  players = prepare_list_of_players()
  play_bites = Bites(ANTS, TOKENS_FOR_TRAIL, players)
  play_bites.play_full_game()

if __name__ == '__main__':
  # play_bites = Bites(ANTS, TOKENS_FOR_TRAIL, prepare_list_of_players())
  start_new_game()