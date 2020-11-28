import unittest
from unittest import mock
from unittest.mock import patch, call
from player import Player
import wine
from constants import ANTHILL_CARD_DICT

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

  def test_check_can_receive_wine_when_not_already_in_hand(self):
    # test 156
    mario = Player("Mario")
    mario.hand = {"apple": 2}
    food = "wine"
    expected_new_hand = {"apple": 2, "wine": 1}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)
    
  def test_check_can_receive_wine_when_already_has_wine_in_hand(self):
    # test 157
    mario = Player("Mario")
    mario.hand = {"wine": 1}
    food = "wine"
    expected_new_hand = {"wine": 2}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)

class ScoreStandardFoodInHandTest(unittest.TestCase):
  def test_can_score_four_points_for_one_token_in_top_slot(self):
    # test 22
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"pepper": 1}
    expected_score = 4
    actual_score = mario.score_standard_food_in_hand(anthill)
    self.assertEqual(actual_score, expected_score)

  def test_can_score_three_points_for_one_token_in_second_top_slot(self):
    # test 23
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"bread": 1}
    expected_score = 3
    actual_score = mario.score_standard_food_in_hand(anthill)
    self.assertEqual(actual_score, expected_score)

  def test_can_score_four_points_for_two_tokens_in_middle_slot(self):
    # test 24
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"cheese": 2}
    expected_score = 4
    actual_score = mario.score_standard_food_in_hand(anthill)
    self.assertEqual(actual_score, expected_score)

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
    actual_score = mario.score_standard_food_in_hand(anthill)
    self.assertEqual(actual_score, expected_score)

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
    actual_score = mario.score_standard_food_in_hand(anthill)
    self.assertEqual(actual_score, expected_score)

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
    actual_score = mario.score_standard_food_in_hand(anthill)
    self.assertEqual(actual_score, expected_score)

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
    actual_score_a = mario.score_standard_food_in_hand(anthill_a)
    actual_score_b = luigi.score_standard_food_in_hand(anthill_b)
    self.assertNotEqual(actual_score_a, actual_score_b)
    self.assertEqual(actual_score_a, expected_score_a)
    self.assertEqual(actual_score_b, expected_score_b)

  def test_wine_in_hand_does_not_affect_standard_score_calc(self):
    # test 163
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {
      "apple": 3,
      "grapes": 4,
      "cheese": 0,
      "bread": 1,
      "pepper": 2,
      "wine": 2}
    expected_standard_score = 15
    actual_standard_score = mario.score_standard_food_in_hand(anthill)
    self.assertEqual(actual_standard_score, expected_standard_score)

class MakeChoiceTest(unittest.TestCase):
  def test_returns_user_input_for_input_is_red(self):
    # test 37
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    prompt_text = "please enter your choice of ant"
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', return_value = "red")
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()
    print_patcher.stop()

  def test_raises_error_with_wrong_colour_input(self):
    # test 38
    """
    Test 38 has been superceeded by test 40; function no longer raises 
    an error since the while loop was added
    """
    pass
    # allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    # input_patcher = mock.patch('builtins.input', return_value = "blue")
    # input_mock = input_patcher.start()
    # self.assertRaises(ValueError, choose_ant_to_move, allowed_choices)
    # input_mock.assert_called_once_with("Pick something: ")
    # input_patcher.stop()

  def test_returns_user_input_for_input_is_yellow(self):
    # test 39
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    prompt_text = "please enter your choice of ant"
    expected_result = "yellow"
    input_patcher = mock.patch('builtins.input', return_value = "yellow")
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()
    print_patcher.stop()

  def test_user_can_make_another_choice_if_wrong_input(self):
    # test 40
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    prompt_text = "please enter your choice of ant"
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', side_effect = ["blue", "red"])
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()
    print_patcher.stop()

  def test_addresses_user_by_name_when_asking_for_ant_choice(self):
    # test 45
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    prompt_text = "please enter your choice of ant"
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', return_value = "red")
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    input_mock.assert_called_once_with("mario; please enter your choice of ant: ")
    input_patcher.stop()
    print_patcher.stop()

  def test_allowed_choices_are_listed_when_choosing_ant(self):
    # test 97
    mario = Player("mario")
    allowed_choices = ["red", "yellow"]
    prompt_text = "please enter your choice of ant"
    print_patcher = mock.patch('builtins.print')
    input_patcher = mock.patch('builtins.input', return_value = "red")
    print_mock = print_patcher.start()
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertGreaterEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[1], mock.call("red"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("yellow"))
    print_patcher.stop()
    input_patcher.stop()

  def test_returns_user_input_for_input_is_front(self):
    # test 41
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    prompt_text = "please pick a direction to collect food from"
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', return_value = "front")
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()
    print_patcher.stop

  def test_returns_user_input_for_input_is_back(self):
    # test 42
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    prompt_text = "please pick a direction to collect food from"
    expected_result = "back"
    input_patcher = mock.patch('builtins.input', return_value = "back")
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()
    print_patcher.stop()
  
  def test_raises_error_with_wrong_direction_input(self):
    # test 43
    """
    Test 43 has been superceeded by test 44; function no longer raises 
    an error since the while loop was added
    """
    pass
    # mario = Player("placeholder name")
    # allowed_choices = ['front', 'back']
    # input_patcher = mock.patch('builtins.input', return_value = "fromt")
    # input_mock = input_patcher.start()
    # self.assertRaises(ValueError, mario.choose_direction_to_pick_food, allowed_choices)
    # input_mock.assert_called_once_with("Pick a direction: ")
    # input_patcher.stop()

  def test_user_can_make_another_choice_if_typo_during_input(self):
    # test 44
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    prompt_text = "please pick a direction to collect food from"
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', side_effect = ["fromt", "front"])
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()
    print_patcher.stop()

  def test_addresses_user_by_name_when_asking_for_direction_choice(self):
    # test 46
    mario = Player("mario")
    allowed_choices = ['front', 'back']
    prompt_text = "please pick a direction to collect food from"
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', return_value = "front")
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    input_mock.assert_called_once_with("mario; please pick a direction to collect food from: ")
    input_patcher.stop()
    print_patcher.stop()

  def test_allowed_choices_are_listed_when_choosing_direction(self):
    # test 98
    mario = Player("mario")
    allowed_choices = ["front", "back"]
    prompt_text = "please enter your choice of ant"
    print_patcher = mock.patch('builtins.print')
    input_patcher = mock.patch('builtins.input', return_value = "front")
    print_mock = print_patcher.start()
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertGreaterEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[1], mock.call("front"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("back"))
    print_patcher.stop()
    input_patcher.stop()

  def test_check_make_choice_allows_user_to_choose_food_from_anthill(self):
    # test 123
    mario = Player("Mario")
    allowed_choices = ["cheese", "grapes"]
    prompt_text = "please enter your choice of food"
    print_patcher = mock.patch('builtins.print')
    input_patcher = mock.patch('builtins.input', return_value = "cheese")
    print_mock = print_patcher.start()
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(print_mock.call_count, 3)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nThe available options are:"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("cheese"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("grapes"))
    self.assertEqual(input_mock.call_count, 1)
    self.assertEqual(input_mock.call_args_list[0], mock.call("Mario; please enter your choice of food: "))
    self.assertEqual(mario.user_choice, "cheese")
    print_patcher.stop()
    input_patcher.stop()

  @patch('builtins.input', return_value = "3")
  @patch('builtins.print')
  def test_user_can_select_an_anthill_level_for_anthill_filling_rule_user_choice(
    self, mock_builtin_input, mock_builtin_print):
    # test 152
    mario = Player("Mario")
    allowed_choices = ['0','1','2','3','4']
    prompt_text = "please enter your choice of anthill level"
    expected_user_choice = "3"
    actual_user_choice = mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(actual_user_choice, expected_user_choice)

class MoveAntAlongTrailTest(unittest.TestCase):
  def test_can_move_onto_trail_of_length_one(self):
    # test 10
    mario = Player("mario")
    trail = ["apple"]
    ant_positions = {"red": None}
    ant = "red"
    expected_new_ant_positions = {"red": 0}
    self.assertEqual(mario.move_ant_along_trail(trail, ant_positions, ant), expected_new_ant_positions)

  def test_can_move_onto_adjacent_position(self):
    # test 11
    mario = Player("mario")
    ant_positions = {"red": 0}
    trail = ["apple", "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 1}
    self.assertEqual(mario.move_ant_along_trail(trail, ant_positions, ant), expected_new_ant_positions)

  def test_ant_moves_past_wrong_food_tokens(self):
    # test 12
    mario = Player("mario")
    ant_positions = {"red": 0}
    trail = ["apple", "grapes", "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 2}
    self.assertEqual(mario.move_ant_along_trail(trail, ant_positions, ant), expected_new_ant_positions)

  def test_ant_moves_past_missing_food_tokens(self):
    # test 13
    mario = Player("mario")
    ant_positions = {"red": 0}
    trail = ["apple", None, "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 2}
    self.assertEqual(mario.move_ant_along_trail(trail, ant_positions, ant), expected_new_ant_positions)

  def test_only_intended_ant_moves(self):
    # test 14
    mario = Player("mario")
    ant_positions = {"red": 0, "purple": 1}
    trail = ["apple", "grapes", "apple"]
    ant = "red"
    expected_new_ant_positions = {"red": 2, "purple": 1}
    self.assertEqual(mario.move_ant_along_trail(trail, ant_positions, ant), expected_new_ant_positions)

class PlaceAntOnAnthillTest(unittest.TestCase):
  """Anthill filling order is top-to-bottom
  """
  def test_first_ant_is_red_and_goes_to_top_spot(self):
    # test 32
    mario = Player("mario")
    ant_positions = {"red": 39}
    anthill = [None, None, None, None, None]
    anthill_rule = "top down"
    ant = "red"
    expected_new_anthill = [None, None, None, None, "red"]
    expected_new_ant_positions = {"red": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  def test_first_ant_is_green_and_goes_to_top_spot(self):
    # test 33
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, None]
    anthill_rule = "top down"
    ant = "green"
    expected_new_anthill = [None, None, None, None, "green"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  def test_top_spot_occupied_second_ant_is_added(self):
    # test 34
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, "red"]
    anthill_rule = "top down"
    ant = "green"
    expected_new_anthill = [None, None, None, "green", "red"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  def test_four_spots_occupied_add_fifth_ant(self):
    # test 35
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, "purple", "yellow", "brown", "red"]
    anthill_rule = "top down"
    ant = "green"
    expected_new_anthill = ["green", "purple", "yellow", "brown", "red"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  def test_ant_position_is_updated_to_show_it_is_on_anthill(self):
    # test 50
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, None]
    anthill_rule = "top down"
    ant = "green"
    expected_new_anthill = [None, None, None, None, "green"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  """Anthill filling order is bottom-to-top
  """
  def test_first_ant_is_red_and_goes_to_bottom_spot(self):
    # test 132
    mario = Player("mario")
    ant_positions = {"red": 39}
    anthill = [None, None, None, None, None]
    anthill_rule = "bottom up"
    ant = "red"
    expected_new_anthill = ["red", None, None, None, None]
    expected_new_ant_positions = {"red": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  def test_first_ant_is_green_and_goes_to_bottom_spot(self):
    # test 133
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, None]
    anthill_rule = "bottom up"
    ant = "green"
    expected_new_anthill = ["green", None, None, None, None]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  def test_bottom_spot_occupied_second_ant_is_added(self):
    # test 134
    mario = Player("Mario")
    ant_positions = {"green": 39}
    anthill = ["red", None, None, None, None]
    anthill_rule = "bottom up"
    ant = "green"
    expected_new_anthill = ["red", "green", None, None, None]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  def test_check_spots_0_to_3_occupied_add_fifth_ant(self):
    # test 135
    mario = Player("Mario")
    ant_positions = {"green": 39}
    anthill = ["red", "purple", "yellow", "brown", None]
    anthill_rule = "bottom up"
    ant = "green"
    expected_new_anthill = ["red", "purple", "yellow", "brown", "green"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant), expected_tuple)

  """Anthill filling order is 4-2-0-3-1
  """
  def test_check_ants_can_fill_anthill_in_order_4_2_0_3_1(self):
    # test 136
    starting_ant_positions = {"red": None, "green": None, "yellow": None, "purple": None, "brown": None}
    starting_anthill = [None, None, None, None, None]
    anthill_rule = "leave gaps"
    first_ant = "red"

    anthill_after_turn_1 =[None, None, None, None, "red"]
    ant_pos_after_turn_1 = {"red": "anthill", "green": None, "yellow": None, "purple": None, "brown": None}
    secont_ant = "green"

    anthill_after_turn_2 = [None, None, "green", None, "red"]
    ant_pos_after_turn_2 = {"red": "anthill", "green": "anthill", "yellow": None, "purple": None, "brown": None}
    third_ant = "yellow"

    anthill_after_turn_3 = ["yellow", None, "green", None, "red"]
    ant_pos_after_turn_3 = {"red": "anthill", "green": "anthill", "yellow": "anthill", "purple": None, "brown": None}
    fourth_ant = "purple"

    anthill_after_turn_4 = ["yellow", None, "green", "purple", "red"]
    ant_pos_after_turn_4 = {"red": "anthill", "green": "anthill", "yellow": "anthill", "purple": "anthill", "brown": None}
    fifth_ant = "brown"

    anthill_after_turn_5 = ["yellow", "brown", "green", "purple", "red"]
    ant_pos_after_turn_5 = {"red": "anthill", "green": "anthill", "yellow": "anthill", "purple": "anthill", "brown": "anthill"}

    expected_end_anthill = anthill_after_turn_5
    expected_end_ant_pos = ant_pos_after_turn_5

    mario = Player("Mario")

    self.assertEqual(mario.place_ant_on_anthill(
      starting_ant_positions, starting_anthill, anthill_rule, first_ant), (
        anthill_after_turn_1, ant_pos_after_turn_1))
    self.assertEqual(mario.place_ant_on_anthill(
      ant_pos_after_turn_1, anthill_after_turn_1, anthill_rule , secont_ant), (
        anthill_after_turn_2, ant_pos_after_turn_2))
    self.assertEqual(mario.place_ant_on_anthill(
      ant_pos_after_turn_2, anthill_after_turn_2, anthill_rule, third_ant), (
        anthill_after_turn_3, ant_pos_after_turn_3))
    self.assertEqual(mario.place_ant_on_anthill(
      ant_pos_after_turn_3, anthill_after_turn_3, anthill_rule, fourth_ant), (
        anthill_after_turn_4, ant_pos_after_turn_4))
    self.assertEqual(mario.place_ant_on_anthill(
      ant_pos_after_turn_4, anthill_after_turn_4, anthill_rule, fifth_ant), (
        expected_end_anthill, expected_end_ant_pos))

  """Test 141 not specific to any anthill filling rule
  """
  def test_anthill_rule_is_received_as_string_and_cross_referenced_with_constants(self):
    # test 141
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, None]
    anthill_rule = "bottom up"
    ant = "green"

    expected_type_of_anthill_rule = str
    expected_dict_lookup_return = [0, 1, 2, 3, 4]

    mario.place_ant_on_anthill(ant_positions, anthill, anthill_rule, ant)

    actual_type_of_anthill_rule = type(anthill_rule)
    actual_dict_lookup_return = ANTHILL_CARD_DICT[anthill_rule]

    self.assertEqual(actual_type_of_anthill_rule, expected_type_of_anthill_rule)
    self.assertEqual(actual_dict_lookup_return, expected_dict_lookup_return)

  """Anthill filling rule is 'user choice'
  """
  @patch('builtins.input', return_value = "3")
  @patch('builtins.print')
  def test_when_filling_rule_is_user_choice_place_ant_on_anthill_gets_user_input_and_places_ant_there(
    self, mock_builtin_print, mock_builtin_input):
    # test 153
    mario = Player("Mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, None]
    anthill_rule = "user choice"
    ant = "green"

    expected_input_call = call("Mario; please enter your choice of anthill level: ")
    expected_new_anthill = [None, None, None, "green", None]
    expected_new_ant_positions = {"green": "anthill"}

    (actual_new_anthill, actual_new_ant_positions) = mario.place_ant_on_anthill(
      ant_positions, anthill, anthill_rule, ant)

    self.assertEqual(mock_builtin_input.call_args_list[0], expected_input_call)
    self.assertEqual(actual_new_anthill, expected_new_anthill)
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)

class TakeFoodFromTrailTest(unittest.TestCase):
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
    self.assertEqual(mario.take_food_from_trail(trail, ant_positions, ant, direction), expected_tuple)

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
    self.assertEqual(mario.take_food_from_trail(trail, ant_positions, ant, direction), expected_tuple)

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
    self.assertEqual(mario.take_food_from_trail(trail, ant_positions, ant, direction), expected_tuple)

  def test_raises_value_error_if_direction_is_wrong(self):
    # test 18
    mario = Player("mario")
    trail = ["apple", "grapes", "cheese", "bread"]
    ant_positions = {"purple": 1, "yellow": 2}
    ant = "purple"
    direction = "forwards"
    self.assertRaises(ValueError, mario.take_food_from_trail, trail, ant_positions, ant, direction)

  def test_None_is_not_collected(self):
    # test 95
    mario = Player("mario")
    trail = ["apple", "grapes", None, "cheese", "bread"]
    ant_positions = {"purple": 1, "yellow": 3}
    ant = "purple"
    direction = "front"
    expected_food = "bread"
    expected_new_trail = ["apple", "grapes", None, "cheese", None]
    expected_tuple = (expected_food, expected_new_trail)
    self.assertEqual(mario.take_food_from_trail(trail, ant_positions, ant, direction), expected_tuple)

  def test_check_wine_can_be_collected_from_trail(self):
    # test 155
    mario = Player("mario")
    trail = ["apple", "grapes", "wine"]
    ant_positions = {"purple": 1}
    ant = "purple"
    direction = "front"
    expected_food = "wine"
    expected_new_trail = ["apple", "grapes", None]
    expected_tuple = (expected_food, expected_new_trail)
    self.assertEqual(mario.take_food_from_trail(trail, ant_positions, ant, direction), expected_tuple)

class DefineAllowedChoicesAntsTest(unittest.TestCase):
  def test_define_allowed_choices_ants_returns_a_list(self):
    # test 52
    mario = Player("mario")
    ant_positions = {"green": None}
    self.assertIsInstance(mario.define_allowed_choices_ants(ant_positions), list)

  def test_one_ant_hasnt_moved_yet_list_contains_that_choice(self):
    # test 53
    mario = Player("mario")
    ant_positions = {"green": None}
    expected_allowed_choices = ["green"]
    self.assertEqual(mario.define_allowed_choices_ants(ant_positions), expected_allowed_choices)

  def test_one_ant_on_trail_list_contains_that_choice(self):
    # test 54
    mario = Player("mario")
    ant_positions = {"green": 39}
    expected_allowed_choices = ["green"]
    self.assertEqual(mario.define_allowed_choices_ants(ant_positions), expected_allowed_choices)

  def test_two_valid_ants_list_contains_both_choices(self):
    # test 55
    mario = Player("mario")
    ant_positions = {"green": 39, "red": None}
    expected_allowed_choices = ["green", "red"]
    self.assertEqual(mario.define_allowed_choices_ants(ant_positions), expected_allowed_choices)

  def test_single_ant_already_on_anthill_is_not_included(self):
    # test 56
    mario = Player("mario")
    ant_positions = {"green": "anthill"}
    expected_allowed_choices = []
    self.assertEqual(mario.define_allowed_choices_ants(ant_positions), expected_allowed_choices)

  def test_ants_at_start_and_on_trail_and_on_anthill_includes_only_ants_at_start_and_on_trail(self):
    # test 57
    mario = Player("mario")
    ant_positions = {"green": None, "red": 39, "purple": "anthill"}
    expected_allowed_choices = ["green", "red"]
    self.assertEqual(mario.define_allowed_choices_ants(ant_positions), expected_allowed_choices)

class DefineAllowedChoicesDirectionTest(unittest.TestCase):
  def test_define_allowed_choices_direction_returns_a_list(self):
    # test 58
    mario = Player("mario")
    ant = "red"
    trail = ["pepper", "apple", "cheese"]
    ant_positions = {"red": 1}
    self.assertIsInstance(mario.define_allowed_choices_direction(ant, trail, ant_positions), list)

  def test_ant_has_valid_choices_immediately_adjacent_in_both_directions(self):
    # test 59
    mario = Player("mario")
    ant = "red"
    trail = ["pepper", "apple", "cheese"]
    ant_positions = {"red": 1}
    expected_allowed_choices = ["front", "back"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)

  def test_ant_has_valid_choice_only_in_front_does_not_return_back(self):
    # test 60
    mario = Player("mario")
    ant = "green"
    trail = ["pepper", "apple", "cheese"]
    ant_positions = {"green": 0}
    expected_allowed_choices = ["front"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertNotIn("back", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_ant_has_valid_choice_only_behind_does_not_return_front(self):
    # test 61
    mario = Player("mario")
    ant = "yellow"
    trail = ["pepper", "apple", "cheese"]
    ant_positions = {"yellow": 2}
    expected_allowed_choices = ["back"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertNotIn("front", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_ant_is_in_trail_but_has_only_empty_spaces_behind_returns_only_front(self):
    # test 62
    mario = Player("mario")
    ant = "green"
    trail = [None, "pepper", "apple", "cheese"]
    ant_positions = {"green": 1}
    expected_allowed_choices = ["front"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertNotIn("back", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_ant_is_in_trail_but_has_only_empty_spaces_in_front_returns_only_back(self):
    # test 63
    mario = Player("mario")
    ant = "yellow"
    trail = ["pepper", "apple", "cheese", None]
    ant_positions = {"yellow": 2}
    expected_allowed_choices = ["back"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertNotIn("front", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_presence_of_other_ants_invalidates_food_so_direction_back_not_included(self):
    # test 64
    mario = Player("mario")
    ant = "green"
    trail = [None, "grapes", None, "pepper", "apple", "cheese"]
    ant_positions = {"green": 3, "purple": 1}
    expected_allowed_choices = ["front"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertNotIn("back", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_presence_of_other_ants_invalidates_food_so_direction_front_not_included(self):
    # test 65
    mario = Player("mario")
    ant = "yellow"
    trail = ["pepper", "apple", "cheese", None, "grapes", None]
    ant_positions = {"yellow": 2, "purple": 4}
    expected_allowed_choices = ["back"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertNotIn("front", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_direction_back_is_allowed_when_multiple_of_the_same_kind_of_food_and_the_first_one_has_an_ant(self):
    # test 113
    mario = Player("Mario")
    ant = "purple"
    trail = ['bread', None, 'cheese', None, 'pepper', None, 'cheese', 'grapes', 'apple']
    ant_positions = {
      "purple": 7,
      "brown": 0,
      "yellow": 2,
      "green": 4}
    expected_allowed_choices = ["front", "back"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertIn("back", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_check_direction_back_is_allowed_in_simplified_version_of_multiple_of_the_same_kind_of_food_and_first_one_has_an_ant(self):
    # test 114
    mario = Player("Mario")
    ant = "purple"
    trail = ['cheese', 'cheese', 'grapes']
    ant_positions = {
      "purple": 2,
      "yellow": 0}
    expected_allowed_choices = ["back"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertIn("back", mario.define_allowed_choices_direction(ant, trail, ant_positions))

  def test_check_direction_front_is_allowed_in_simple_version_of_multiple_of_the_same_kind_of_food_and_ant_is_on_first_one(self):
    # test 115
    mario = Player("Mario")
    ant = "purple"
    trail = ['grapes','cheese', 'cheese']
    ant_positions = {
      "purple": 0,
      "yellow": 1}
    expected_allowed_choices = ["front"]
    self.assertEqual(mario.define_allowed_choices_direction(ant, trail, ant_positions), expected_allowed_choices)
    self.assertIn("front", mario.define_allowed_choices_direction(ant, trail, ant_positions))

class TakeTurnTest(unittest.TestCase):
  def test_single_ant_moves_to_centre_of_three_element_trail_picks_front(self):
    # test 66
    # Given
    anthill = [None]
    mario = Player("mario")
    trail = ["pepper", "apple", "cheese"]
    ant_positions = {"red": None}
    anthill_rule = [4, 3, 2, 1, 0]
    anthill_food_tokens = {}
    input_patcher = mock.patch('builtins.input', side_effect = ["red", "front"])
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    # When
    (actual_new_trail, actual_new_ant_positions, actual_new_anthill, actual_new_anthill_food) = \
      mario.take_turn(trail, ant_positions, anthill, anthill_rule, anthill_food_tokens)
    # Then
    expected_new_hand = {"cheese": 1}
    expected_new_trail = ["pepper", "apple", None]
    expected_new_ant_positions = {"red": 1}
    expected_new_anthill = [None]
    self.assertEqual(actual_new_trail, expected_new_trail)
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)
    self.assertEqual(actual_new_anthill, expected_new_anthill)
    self.assertEqual(mario.hand, expected_new_hand)
    input_patcher.stop()
    print_patcher.stop()

  def test_single_ant_moves_from_centre_of_three_element_trail_onto_anthill(self):
    # test 67
    # Given
    anthill = [None]
    mario = Player("mario")
    mario.hand = {"cheese": 1}
    trail = ["pepper", "apple", None]
    ant_positions = {"red": 1}
    anthill_food_tokens = {"pepper": 1, "bread": 1}
    anthill_rule = "bottom up"
    user_choice_ant = "red"
    user_choice_anthill_food = "bread"
    input_patcher = mock.patch('builtins.input', side_effect = [user_choice_ant, user_choice_anthill_food])
    print_patcher = mock.patch('builtins.print')
    input_mock = input_patcher.start()
    print_mock = print_patcher.start()
    # When
    (actual_new_trail, actual_new_ant_positions, actual_new_anthill, actual_new_anthill_food) = \
      mario.take_turn(trail, ant_positions, anthill, anthill_rule, anthill_food_tokens)
    # Then
    expected_new_trail = trail
    expected_new_ant_positions = {"red": "anthill"}
    expected_new_anthill = ["red"]
    expected_new_anthill_food = {"pepper": 1, "bread": 0}
    expected_new_hand = {"cheese": 1, "bread": 1}
    self.assertEqual(actual_new_trail, expected_new_trail)
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)
    self.assertEqual(actual_new_anthill, expected_new_anthill)
    self.assertEqual(mario.hand, {"cheese": 1, "bread": 1})
    self.assertEqual(actual_new_anthill_food, expected_new_anthill_food)
    input_patcher.stop()
    print_patcher.stop()

class GoesToAnthillTest(unittest.TestCase):
  def test_returns_true_when_ant_is_at_end_of_trail(self):
    # test 68
    mario = Player("mario")
    trail = ["pepper", "apple", "cheese"]
    ant = "yellow"
    ant_positions = {"yellow": 2}
    actual_return = mario.goes_to_anthill(ant, trail, ant_positions)
    expected_return = True
    self.assertEqual(actual_return, expected_return)

  def test_returns_false_when_ant_is_not_at_end_of_trail_and_correct_food_is_in_front_of_it(self):
    # test 69
    mario = Player("mario")
    trail = ["pepper", "apple", "cheese", "pepper", "apple", "cheese"]
    ant = "yellow"
    ant_positions = {"yellow": 2}
    actual_return = mario.goes_to_anthill(ant, trail, ant_positions)
    expected_return = False
    self.assertEqual(actual_return, expected_return)

  def test_returns_false_when_ant_is_before_trail_and_correct_food_is_in_trail(self):
    # test 70
    mario = Player("mario")
    trail = ["pepper", "apple", "cheese", "pepper", "apple"]
    ant = "yellow"
    ant_positions = {"yellow": None}
    actual_return = mario.goes_to_anthill(ant, trail, ant_positions)
    expected_return = False
    self.assertEqual(actual_return, expected_return)

  def test_returns_true_when_ant_is_before_trail_and_correct_food_is_not_in_trail(self):
    # test 71
    mario = Player("mario")
    trail = ["pepper", "apple", "pepper", "apple"]
    ant = "yellow"
    ant_positions = {"yellow": None}
    actual_return = mario.goes_to_anthill(ant, trail, ant_positions)
    expected_return = True
    self.assertEqual(actual_return, expected_return)

  def test_ant_is_not_at_end_but_none_of_correct_food_remains_in_trail(self):
    # test 72
    mario = Player("mario")
    trail = ["pepper", "apple", "pepper", "cheese", "apple"]
    ant = "yellow"
    ant_positions = {"yellow": 3}
    actual_return = mario.goes_to_anthill(ant, trail, ant_positions)
    expected_return = True
    self.assertEqual(actual_return, expected_return)

class DefineAllowedChoicesAnthillFoodTest(unittest.TestCase):
  def test_define_allowed_choices_anthill_test_returns_a_list(self):
    # test 119
    mario = Player("Mario")
    anthill_food_tokens = {}
    self.assertIsInstance(mario.define_allowed_choices_anthill_food(
      anthill_food_tokens), list)

  def test_anthill_has_one_token_and_allowed_choices_shows_this_token(self):
    # test 120
    mario = Player("Mario")
    anthill_food_tokens = {"cheese": 1}
    expected_allowed_choices = ["cheese"]
    self.assertEqual(mario.define_allowed_choices_anthill_food(
      anthill_food_tokens), expected_allowed_choices)

  def test_anthill_has_one_each_of_two_types_of_food_allowed_choices_shows_both(self):
    # test 121
    mario = Player("Mario")
    anthill_food_tokens = {"cheese": 1, "bread": 1}
    expected_allowed_choices = [["cheese", "bread"], ["bread", "cheese"]]
    self.assertIn(mario.define_allowed_choices_anthill_food(
      anthill_food_tokens), expected_allowed_choices)

  def test_anthill_has_had_one_token_removed_so_v_is_0_for_one_item_this_item_should_not_be_included(self):
    # test 122
    mario = Player("Mario")
    anthill_food_tokens = {"cheese": 1, "bread": 0}
    expected_allowed_choices = ["cheese"]
    self.assertEqual(mario.define_allowed_choices_anthill_food(
      anthill_food_tokens), expected_allowed_choices)

class TakeFoodFromAnthillTest(unittest.TestCase):
  def test_anthill_has_one_food_and_player_takes_it(self):
    # test 124
    mario = Player("Mario")
    anthill_food = {"cheese": 1}
    user_choice_food = "cheese"
    expected_new_anthill_food = {"cheese": 0}
    actual_new_anthill_food = mario.take_food_from_anthill(anthill_food, user_choice_food)
    self.assertEqual(actual_new_anthill_food, expected_new_anthill_food)

  def test_anthill_has_one_each_of_two_food_types_user_picks_one(self):
    # test 125
    mario = Player("Mario")
    anthill_food = {"cheese": 1, "apple": 1}
    user_choice_food = "cheese"
    expected_new_anthill_food = {"cheese": 0, "apple": 1}
    actual_new_anthill_food = mario.take_food_from_anthill(anthill_food, user_choice_food)
    self.assertEqual(actual_new_anthill_food, expected_new_anthill_food)

  def test_check_anthill_has_2_of_user_choice_food_and_new_food_dict_has_1(self):
    # test 126
    mario = Player("Mario")
    anthill_food = {"cheese": 2, "apple": 1}
    user_choice_food = "cheese"
    expected_new_anthill_food = {"cheese": 1, "apple": 1}
    actual_new_anthill_food = mario.take_food_from_anthill(anthill_food, user_choice_food)
    self.assertEqual(actual_new_anthill_food, expected_new_anthill_food)

class DefineAllowedChoicesAnthillPlacementTest(unittest.TestCase):
  def test_define_allowed_choices_anthill_placement_returns_list(self):
    # test 146
    mario = Player("Mario")
    anthill = []
    self.assertIsInstance(mario.define_allowed_choices_anthill_placement(anthill), list)

  def test_anthill_is_empty_and_allowed_choices_returns_all_indices(self):
    # test 147
    mario = Player("Mario")
    anthill = [None, None, None, None, None]
    expected_allowed_choices = ['0','1','2','3','4']
    actual_allowed_choices = mario.define_allowed_choices_anthill_placement(anthill)
    self.assertEqual(actual_allowed_choices, expected_allowed_choices)

  def test_anthill_has_only_top_spot_occupied_returns_all_other_indices(self):
    # test 148
    mario = Player("Mario")
    anthill = [None, None, None, None, "purple"]
    expected_allowed_choices = ['0','1','2','3']
    actual_allowed_choices = mario.define_allowed_choices_anthill_placement(anthill)
    self.assertEqual(actual_allowed_choices, expected_allowed_choices)

  def test_check_anthill_has_one_occupied_slot_at_level_three(self):
    # test 149
    mario = Player("Mario")
    anthill = [None, None, None, "purple", None]
    expected_allowed_choices = ['0','1','2','4']
    actual_allowed_choices = mario.define_allowed_choices_anthill_placement(anthill)
    self.assertEqual(actual_allowed_choices, expected_allowed_choices)
  
  def test_check_anthill_has_multiple_occupied_slots(self):
    # test 150
    mario = Player("Mario")
    anthill = ["red", None, "yellow", "purple", "brown"]
    expected_allowed_choices = ['1']
    actual_allowed_choices = mario.define_allowed_choices_anthill_placement(anthill)
    self.assertEqual(actual_allowed_choices, expected_allowed_choices)

class ScoreHandTest(unittest.TestCase):
  def test_score_hand_updates_player_score_with_combined_std_plus_wine_scores(self):
    # test 162
    mario = Player("Mario")
    mario.hand = {
      "wine": 2,
      "apple": 3,
      "grapes": 2,
      "bread": 1,    }
    anthill = ["brown", "yellow", "purple", "green", "red"]
    standard_tokens_for_trail = {
      "apple": 0,
      "grapes": 0,
      "cheese": 0,
      "bread": 0,
      "pepper": 0}
    
    wine_rule = "collector"
    standard_food_score = 16
    wine_score = 6
    expected_score = standard_food_score + wine_score
    mario.score_hand(anthill, standard_tokens_for_trail, wine_rule)

    self.assertEqual(mario.score, expected_score)

  def test_score_hand_updates_player_score_for_hand_with_no_wine_only_standard_food(self):
    # test 164
    """Test superceeded by refactoring the 0 wine case into the general score_wine() method
    """
    pass
    # mario = Player("Mario")
    # mario.hand = {
    #   "apple": 3,
    #   "grapes": 2,
    #   "bread": 1,    }
    # anthill = ["brown", "yellow", "purple", "green", "red"]
    # standard_tokens_for_trail = {
    #   "apple": 0,
    #   "grapes": 0,
    #   "cheese": 0,
    #   "bread": 0,
    #   "pepper": 0}
    
    # standard_food_score = 16
    # wine_score = 0
    # expected_score = standard_food_score + wine_score
    # mario.score_hand(anthill, standard_tokens_for_trail)

    # self.assertEqual(mario.score, expected_score)

  def test_score_hand_updates_player_score_for_hand_with_one_wine_and_standard_food(self):
    # test 165
    mario = Player("Mario")
    mario.hand = {
      "wine": 1,
      "apple": 3,
      "grapes": 2,
      "bread": 1,    }
    anthill = ["brown", "yellow", "purple", "green", "red"]
    standard_tokens_for_trail = {
      "apple": 0,
      "grapes": 0,
      "cheese": 0,
      "bread": 0,
      "pepper": 0}
    
    wine_rule = "collector"
    standard_food_score = 16
    wine_score = 3
    expected_score = standard_food_score + wine_score
    mario.score_hand(anthill, standard_tokens_for_trail, wine_rule)

    self.assertEqual(mario.score, expected_score)

  @patch('player.Player.score_standard_food_in_hand', return_value=16)
  @patch('player.Player.score_wine', return_value=3)
  def test_score_hand_calls_both_score_std_and_score_wine(self, score_wine_mock, score_standard_mock):
    # test 166
    mario = Player("Mario")
    mario.hand = {}
    anthill = []
    standard_tokens_for_trail = {
      "apple": 0,
      "grapes": 0,
      "cheese": 0,
      "bread": 0,
      "pepper": 0}
    wine_rule = "collector"
    mario.score_hand(anthill, standard_tokens_for_trail, wine_rule)

    expected_score = 19

    score_standard_mock.assert_called_once_with(anthill)
    score_wine_mock.assert_called_once_with(standard_tokens_for_trail, wine_rule)
    self.assertEqual(mario.score, expected_score)

class ScoreWineTest(unittest.TestCase):
  def test_score_wine_returns_an_int(self):
    # test 176
    mario = Player("Mario")
    standard_tokens_for_trail = {"apple": 0}
    standard_tokens_for_trail = {}
    wine_rule = ""
    actual_result = mario.score_wine(standard_tokens_for_trail, wine_rule)
    self.assertIsInstance(actual_result, int)

  def test_rule_is_collector_hand_has_1_wine_and_1_food_score_wine_returns_1(self):
    # test 177
    mario = Player("Mario")
    standard_tokens_for_trail = {"apple": 0}
    mario.hand = {"apple": 1, "wine": 1}
    standard_tokens_for_trail = {"apple": 0}
    wine_rule = "collector"
    expected_result = 1
    actual_result = mario.score_wine(standard_tokens_for_trail, wine_rule)
    self.assertEqual(actual_result, expected_result)

  def test_rule_is_collector_hand_has_2_wine_and_1_food_score_wine_returns_2(self):
    # test 178
    mario = Player("Mario")
    mario.hand = {"apple": 1, "wine": 2}
    standard_tokens_for_trail = {"apple": 0}
    wine_rule = "collector"
    expected_result = 2
    actual_result = mario.score_wine(standard_tokens_for_trail, wine_rule)
    self.assertEqual(actual_result, expected_result)

  def test_rule_is_oenophile_hand_has_2_wines_score_wine_returns_4(self):
    # test 179
    mario = Player("Mario")
    mario.hand = {"wine": 2}
    standard_tokens_for_trail = {}
    wine_rule = "oenophile"
    expected_result = 4
    actual_result = mario.score_wine(standard_tokens_for_trail, wine_rule)
    self.assertEqual(actual_result, expected_result)

  def test_score_wine_calls_collector_method_from_constants(self):
    # test 180
    mario = Player("Mario")
    mario.hand = {"apple": 1, "wine": 2}
    standard_tokens_for_trail = {"apple": 0}
    wine_rule = "collector"
    with patch.dict('player.WINE_CARD_DICT', {
      "collector": mock.MagicMock(return_value=2),
      "oenophile": mock.MagicMock(return_value=4),
      }) as const_mock_wine_card:
      actual_wine_score = mario.score_wine(standard_tokens_for_trail, wine_rule)
      const_mock_wine_card["collector"].assert_called_once_with(mario.hand, standard_tokens_for_trail)
    self.assertEqual(actual_wine_score, 2)

  def test_score_wine_calls_oenophile_method_from_constants(self):
    # test 181
    mario = Player("Mario")
    mario.hand = {"apple": 1, "wine": 2}
    standard_tokens_for_trail = {"apple": 0}
    wine_rule = "oenophile"
    with patch.dict('player.WINE_CARD_DICT', {
      "collector": mock.MagicMock(return_value=2),
      "oenophile": mock.MagicMock(return_value=4),
      }) as const_mock_wine_card:
      actual_wine_score = mario.score_wine(standard_tokens_for_trail, wine_rule)
      const_mock_wine_card["oenophile"].assert_called_once_with(mario.hand, standard_tokens_for_trail)
    self.assertEqual(actual_wine_score, 4)

class SpendChocolateTest(unittest.TestCase):
  def test_spend_chocolate_can_reduce_chocolate_in_hand_from_5_to_4(self):
    # test 195
    mario = Player("Mario")
    mario.hand = {"chocolate": 5}
    
    expected_new_hand = {"chocolate": 4}
    actual_new_hand = mario.spend_chocolate()

    self.assertEqual(actual_new_hand, expected_new_hand)

  def test_spend_chocolate_can_reduce_chocolate_in_hand_from_3_to_2(self):
    # test 196
    mario = Player("Mario")
    mario.hand = {"chocolate": 3}
    
    expected_new_hand = {"chocolate": 2}
    actual_new_hand = mario.spend_chocolate()

    self.assertEqual(actual_new_hand, expected_new_hand)

  def test_spend_chocolate_returns_same_hand_if_hand_has_no_choc(self):
    # test 197
    mario = Player("Mario")
    mario.hand = {"cheese": 3}
    
    expected_new_hand = {"cheese": 3}
    actual_new_hand = mario.spend_chocolate()

    self.assertEqual(actual_new_hand, expected_new_hand)

  def test_spend_chocolate_removes_chocolate_completely_if_only_1_in_hand(self):
    # test 198
    mario = Player("Mario")
    mario.hand = {"chocolate": 1}
    
    expected_new_hand = {}
    actual_new_hand = mario.spend_chocolate()

    self.assertEqual(actual_new_hand, expected_new_hand)

class AskToSpendChocolateTest(unittest.TestCase):
  @patch('builtins.print')
  @patch('builtins.input', return_value = "yes")
  def test_ask_to_spend_choc_returns_True_for_input_yes(self, mock_builtin_input, mock_builtin_print):
    # test 205
    mario = Player("Mario")
    expected_result = True

    actual_result = mario.ask_to_spend_chocolate()

    self.assertEqual(actual_result, expected_result)
    mock_builtin_input.assert_called_once_with("Would you like to spend a chocolate token?\n")

  @patch('builtins.print')
  @patch('builtins.input', return_value = "no")
  def test_ask_to_spend_choc_returns_False_for_input_no(self, mock_builtin_input, mock_builtin_print):
    # test 206
    mario = Player("Mario")
    expected_result = False

    actual_result = mario.ask_to_spend_chocolate()

    self.assertEqual(actual_result, expected_result)
    mock_builtin_input.assert_called_once_with("Would you like to spend a chocolate token?\n")

  @patch('builtins.print')
  @patch('builtins.input', return_value = "yes")
  def test_ask_to_spend_choc_shows_user_the_options(self, mock_builtin_input, mock_builtin_print):
    # test 207
    mario = Player("Mario")
    mario.ask_to_spend_chocolate()

    mock_builtin_print.assert_called_once_with("Please enter 'yes' or 'no'.")

  @patch('builtins.print')
  @patch('builtins.input', side_effect = ["maybe", "no"])
  def test_ask_to_spend_choc_asks_again_if_incorrect_input(
    self, 
    mock_builtin_input, 
    mock_builtin_print,
    ):
    # test 208
    mario = Player("Mario")

    expected_result = False
    actual_result = mario.ask_to_spend_chocolate()

    self.assertEqual(actual_result, expected_result)
    self.assertEqual(mock_builtin_input.call_args_list[0], call("Would you like to spend a chocolate token?\n"))
    self.assertEqual(mock_builtin_input.call_args_list[1], call("Would you like to spend a chocolate token?\n"))
    self.assertEqual(len(mock_builtin_input.call_args_list), 2)

class WillSpendChocTest(unittest.TestCase):
  @patch('player.Player.ask_to_spend_chocolate', return_value = True)
  def test_will_spend_choc_returns_True_if_choc_in_hand(self, mock_ask):
    # test 209
    mario = Player("Mario")
    mario.hand = {"chocolate": 3}

    expected_return = True
    actual_return = mario.will_spend_choc()

    self.assertEqual(actual_return, expected_return)

  @patch('player.Player.ask_to_spend_chocolate')
  def test_will_spend_choc_returns_False_if_choc_not_in_hand(self, mock_ask):
    # test 210
    mario = Player("Mario")
    mario.hand = {"cheese": 3}

    expected_return = False
    actual_return = mario.will_spend_choc()

    self.assertEqual(actual_return, expected_return)

  @patch('player.Player.ask_to_spend_chocolate')
  def test_will_spend_choc_calls_ask_to_spend_choc(self, mock_ask):
    # test 211
    mario = Player("Mario")
    mario.hand = {"chocolate": 3}

    mario.will_spend_choc()
    mock_ask.assert_called_once_with()

  @patch('player.Player.ask_to_spend_chocolate')
  def test_will_spend_choc_only_calls_ask_to_spend_if_choc_in_hand(self, mock_ask):
    # test 212
    mario = Player("Mario")
    mario.hand = {"cheese": 3}

    mario.will_spend_choc()
    assert not mock_ask.called

class TakeTurboTurnTest(unittest.TestCase):
  # test 213
  @patch('player.Player.make_choice', return_value = "yellow")
  @patch('player.Player.define_allowed_choices_ants', return_value = ["yellow"])
  def test_take_turbo_turn_starts_with_player_choosing_ant(
    self,
    mock_allowed_ants,
    mock_ant_choice,
  ):
    trail = ["cheese", "cheese", "cheese"]
    ant = "yellow"
    ant_positions = {"yellow": 0}
    anthill = [None]
    anthill_rule = ""
    anthill_food_tokens = {"cheese" : 1}
    mario = Player("Mario")

    manager = mock.Mock()
    manager.attach_mock(mock_allowed_ants, 'mock_allowed_ants')
    manager.attach_mock(mock_ant_choice, 'mock_ant_choice')

    mario.take_turbo_turn(trail, ant_positions, anthill, anthill_rule, anthill_food_tokens)

    expected_calls = [
      mock.call.mock_allowed_ants(ant_positions),
      mock.call.mock_ant_choice(["yellow"], "please enter your choice of ant"),
    ]

    self.assertEqual(manager.mock_calls, expected_calls)







if __name__ == '__main__':
  unittest.main(verbosity = 2)
