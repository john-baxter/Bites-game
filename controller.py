def enter_number_of_players():
  number_of_players = 0
  while number_of_players < 2 or number_of_players > 5:
    number_of_players = input()

  return number_of_players