from constants import MIN_PLAYERS, MAX_PLAYERS

def enter_number_of_players():
  number_of_players = 0
  while number_of_players not in range(MIN_PLAYERS, MAX_PLAYERS+1):
    number_of_players = input()

  return number_of_players