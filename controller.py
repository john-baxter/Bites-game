from constants import MIN_PLAYERS, MAX_PLAYERS
from player import Player

def enter_number_of_players():
  number_of_players = 0
  while number_of_players not in range(MIN_PLAYERS, MAX_PLAYERS+1):
    number_of_players = input("Please enter the number of players: ")

  return number_of_players

def generate_player():
  name = input("Please enter your name: ")
  player = Player(name)
  return player

def prepare_list_of_players():
  return []