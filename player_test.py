import unittest
from unittest import mock
from player import Player

class PlayerInitTest(unittest.TestCase):
  def test___init___method_works(self):
  # test 30
  # This test was written rertrospectively; the __init__ method came about 
  # naturally during refactoring of the code into the Player class.
    mario = Player("placeholder name")
    expected_mario_hand = {}
    expected_mario_score = 0
    self.assertIsInstance(mario, Player)
    self.assertEqual(mario.hand, expected_mario_hand)
    self.assertEqual(mario.score, expected_mario_score)

  def test_player_instance_has_name(self):
  # test 31
    mario = Player("Mario Mario")
    expected_name = "Mario Mario"
    self.assertEqual(mario.name, expected_name)

class InitialiseHandTest(unittest.TestCase):
  def test_can_initialise_player_hand(self):
  # test 9
    mario = Player("placeholder name")
    self.assertIsInstance(mario.hand, dict)
    self.assertEqual(len(mario.hand), 0)

class StoreFoodTest(unittest.TestCase):
  def test_can_receive_single_food_to_empty_hand(self):
  # test 19
    mario = Player("placeholder name")
    food = "apple"
    expected_new_hand = {"apple": 1}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)

  def test_can_receive_second_token_of_same_food(self):
  # test 20
    mario = Player("placeholder name")
    mario.hand = {"apple": 1}
    food = "apple"
    expected_new_hand = {"apple": 2}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)

  def test_can_receive_food_not_already_in_hand(self):
    # test 21
      mario = Player("placeholder name")
      mario.hand = {"apple": 2}
      food = "cheese"
      expected_new_hand = {"apple": 2, "cheese": 1}
      mario.store_food(food)
      self.assertEqual(mario.hand, expected_new_hand)

class ScoreHandTest(unittest.TestCase):
  def test_can_score_four_points_for_one_token_in_top_slot(self):
  # test 22
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"pepper": 1}
    expected_score = 4
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_three_points_for_one_token_in_second_top_slot(self):
  # test 23
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"bread": 1}
    expected_score = 3
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_four_points_for_two_tokens_in_middle_slot(self):
  # test 24
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"cheese": 2}
    expected_score = 4
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_ten_points_for_one_of_each_token(self):
  # test 25
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {
      "apple": 1,
      "grapes": 1,
      "cheese": 1,
      "bread": 1,
      "pepper": 1}
    expected_score = 10
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_twenty_points_for_two_of_each_token(self):
  # test 26
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {
      "apple": 2,
      "grapes": 2,
      "cheese": 2,
      "bread": 2,
      "pepper": 2}
    expected_score = 20
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_typical_end_of_game_hand_gives_correct_score(self):
  # test 28
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {
      "apple": 3,
      "grapes": 4,
      "cheese": 0,
      "bread": 1,
      "pepper": 2}
    expected_score = 15
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_same_hand_gives_different_scores_for_different_anthill_configurations(self):
  # test 29
    mario = Player("placeholder name")
    luigi = Player("placeholder name")
    anthill_a = ["red", "purple", "yellow", "brown", "green"]
    anthill_b = ["purple", "yellow", "brown", "red", "green"]
    hand = {
      "apple": 3,
      "grapes": 4,
      "cheese": 0,
      "bread": 1,
      "pepper": 2}
    mario.hand = hand
    luigi.hand = hand
    expected_score_a = 15
    expected_score_b = 19
    mario.score_hand(anthill_a)
    luigi.score_hand(anthill_b)
    self.assertNotEqual(mario.score, luigi.score)
    self.assertEqual(mario.score, expected_score_a)
    self.assertEqual(luigi.score, expected_score_b)

class ChooseAntToMoveTest(unittest.TestCase):
  def test_returns_user_input_for_input_is_red(self):
  # test 37
    mario = Player("placeholder name")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', return_value = "red")
    InputMock = input_patcher.start()
    mario.choose_ant_to_move(allowed_choices)
    self.assertEqual(mario.user_choice_ant, expected_result)
    self.assertEqual(InputMock.call_count, 1)
    input_patcher.stop()

  """
  Test 38 has been superceeded by test 40; function no longer raises 
  an error since the while loop was added
  """
  # def test_raises_error_with_wrong_input(self):
  # # test 38
  #   allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
  #   input_patcher = mock.patch('builtins.input', return_value = "blue")
  #   InputMock = input_patcher.start()
  #   self.assertRaises(ValueError, choose_ant_to_move, allowed_choices)
  #   InputMock.assert_called_once_with("Pick something: ")
  #   input_patcher.stop()

  def test_returns_user_input_for_input_is_yellow(self):
  # test 39
    mario = Player("placeholder name")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    expected_result = "yellow"
    input_patcher = mock.patch('builtins.input', return_value = "yellow")
    InputMock = input_patcher.start()
    mario.choose_ant_to_move(allowed_choices)
    self.assertEqual(mario.user_choice_ant, expected_result)
    self.assertEqual(InputMock.call_count, 1)
    input_patcher.stop()

  def test_user_can_make_another_choice_if_wrong_input(self):
  # test 40
    mario = Player("placeholder name")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', side_effect = ["blue", "red"])
    InputMock = input_patcher.start()
    mario.choose_ant_to_move(allowed_choices)
    self.assertEqual(mario.user_choice_ant, expected_result)
    self.assertEqual(InputMock.call_count, 2)
    input_patcher.stop()

  def test_addresses_user_by_name_when_asking_for_ant_choice(self):
  # test 45
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', return_value = "red")
    InputMock = input_patcher.start()
    mario.choose_ant_to_move(allowed_choices)
    self.assertEqual(mario.user_choice_ant, expected_result)
    InputMock.assert_called_once_with("mario; please enter your choice of ant: ")
    input_patcher.stop()

class ChooseDirectionToPickFoodTest(unittest.TestCase):
  def test_returns_user_input_for_input_is_front(self):
  # test 41
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', return_value = "front")
    InputMock = input_patcher.start()
    mario.choose_direction_to_pick_food(allowed_choices)
    self.assertEqual(mario.user_choice_direction, expected_result)
    self.assertEqual(InputMock.call_count, 1)
    input_patcher.stop()

  def test_returns_user_input_for_input_is_back(self):
  # test 42
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    expected_result = "back"
    input_patcher = mock.patch('builtins.input', return_value = "back")
    InputMock = input_patcher.start()
    mario.choose_direction_to_pick_food(allowed_choices)
    self.assertEqual(mario.user_choice_direction, expected_result)
    self.assertEqual(InputMock.call_count, 1)
    input_patcher.stop()
  
  """
  Test 43 has been superceeded by test 44; function no longer raises 
  an error since the while loop was added
  """
  # def test_raises_error_with_wrong_input(self):
  # # test 43
  #   mario = Player("placeholder name")
  #   allowed_choices = ['front', 'back']
  #   input_patcher = mock.patch('builtins.input', return_value = "fromt")
  #   InputMock = input_patcher.start()
  #   self.assertRaises(ValueError, mario.choose_direction_to_pick_food, allowed_choices)
  #   InputMock.assert_called_once_with("Pick a direction: ")
  #   input_patcher.stop()

  def test_user_can_make_another_choice_if_typo_during_input(self):
  # test 44
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', side_effect = ["fromt", "front"])
    InputMock = input_patcher.start()
    mario.choose_direction_to_pick_food(allowed_choices)
    self.assertEqual(mario.user_choice_direction, expected_result)
    self.assertEqual(InputMock.call_count, 2)
    input_patcher.stop()

  def test_addrsses_user_by_name_when_asking_for_direction_choice(self):
  # test 46
    mario = Player("mario")
    allowed_choices = ['front', 'back']
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', return_value = "front")
    InputMock = input_patcher.start()
    mario.choose_direction_to_pick_food(allowed_choices)
    self.assertEqual(mario.user_choice_direction, expected_result)
    InputMock.assert_called_once_with("mario; please pick a direction to collect food from: ")
    input_patcher.stop()

class MoveAntTest(unittest.TestCase):
  def test_can_move_onto_trail_of_length_one(self):
  # test 10
    mario = Player("mario")
    trail = ["apple"]
    ant_positions = {"red": None}
    ant = "red"
    expected_new_ant_positions = {"red": 0}
    self.assertEqual(mario.move_ant(trail, ant_positions, ant), expected_new_ant_positions)

  def test_can_move_onto_adjacent_position(self):
  # test 11
    mario = Player("mario")
    ant_positions = {"red": 0}
    trail = ["apple", "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 1}
    self.assertEqual(mario.move_ant(trail, ant_positions, ant), expected_new_ant_positions)

  def test_ant_moves_past_wrong_food_tokens(self):
  # test 12
    mario = Player("mario")
    ant_positions = {"red": 0}
    trail = ["apple", "grapes", "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 2}
    self.assertEqual(mario.move_ant(trail, ant_positions, ant), expected_new_ant_positions)

  def test_ant_moves_past_missing_food_tokens(self):
  # test 13
    mario = Player("mario")
    ant_positions = {"red": 0}
    trail = ["apple", None, "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 2}
    self.assertEqual(mario.move_ant(trail, ant_positions, ant), expected_new_ant_positions)

  def test_only_intended_ant_moves(self):
  # test 14
    mario = Player("mario")
    ant_positions = {"red": 0, "purple": 1}
    trail = ["apple", "grapes", "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 2, "purple": 1}
    self.assertEqual(mario.move_ant(trail, ant_positions, ant), expected_new_ant_positions)

class PlaceAntOnAnthillTest(unittest.TestCase):
  def test_first_ant_is_red_and_goes_to_top_spot(self):
  # test 32
    mario = Player("mario")
    anthill = [None, None, None, None, None]
    ant = "red"
    expected_new_anthill = [None, None, None, None, "red"]
    self.assertEqual(mario.place_ant_on_anthill(anthill, ant), expected_new_anthill)

  def test_first_ant_is_green_and_goes_to_top_spot(self):
  # test 33
    mario = Player("mario")
    anthill = [None, None, None, None, None]
    ant = "green"
    expected_new_anthill = [None, None, None, None, "green"]
    self.assertEqual(mario.place_ant_on_anthill(anthill, ant), expected_new_anthill)

  def test_top_spot_occupied_second_ant_is_added(self):
  # test 34
    mario = Player("mario")
    anthill = [None, None, None, None, "red"]
    ant = "green"
    expected_new_anthill = [None, None, None, "green", "red"]
    self.assertEqual(mario.place_ant_on_anthill(anthill, ant), expected_new_anthill)

  def test_four_spots_occupied_add_fifth_ant(self):
  # test 35
    mario = Player("mario")
    anthill = [None, "purple", "yellow", "brown", "red"]
    ant = "green"
    expected_new_anthill = ["green", "purple", "yellow", "brown", "red"]
    self.assertEqual(mario.place_ant_on_anthill(anthill, ant), expected_new_anthill)

class TakeFoodTest(unittest.TestCase):
  def test_single_ant_on_trail_can_take_food_in_front(self):
  # test 15
    mario = Player("mario")
    trail = ["apple", "grapes", "cheese"]
    ant_positions = {"purple": 1}
    ant = "purple"
    direction = "front"
    expected_food = "cheese"
    expected_new_trail = ["apple", "grapes", None]
    expected_tuple = (expected_food, expected_new_trail)
    self.assertEqual(mario.take_food(trail, ant_positions, ant, direction), expected_tuple)

  def test_single_ant_on_trail_can_take_food_behind(self):
  # test 16
    mario = Player("mario")
    trail = ["apple", "grapes", "cheese"]
    ant_positions = {"purple": 1}
    ant = "purple"
    direction = "back"
    expected_food = "apple"
    expected_new_trail = [None, "grapes", "cheese"]
    expected_tuple = (expected_food, expected_new_trail)
    self.assertEqual(mario.take_food(trail, ant_positions, ant, direction), expected_tuple)

  def test_adjacent_food_is_blocked_by_presence_of_other_ant(self):
  # test 17
    mario = Player("mario")
    trail = ["apple", "grapes", "cheese", "bread"]
    ant_positions = {"purple": 1, "yellow": 2}
    ant = "purple"
    direction = "front"
    expected_food = "bread"
    expected_new_trail = ["apple", "grapes", "cheese", None]
    expected_tuple = (expected_food, expected_new_trail)
    self.assertEqual(mario.take_food(trail, ant_positions, ant, direction), expected_tuple)

  def test_raises_value_error_if_direction_is_wrong(self):
  # test 18
    mario = Player("mario")
    trail = ["apple", "grapes", "cheese", "bread"]
    ant_positions = {"purple": 1, "yellow": 2}
    ant = "purple"
    direction = "forwards"
    self.assertRaises(ValueError, mario.take_food, trail, ant_positions, ant, direction)

if __name__ == '__main__':
  unittest.main()
