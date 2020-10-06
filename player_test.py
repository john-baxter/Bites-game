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

class MakeChoiceTest(unittest.TestCase):
  def test_returns_user_input_for_input_is_red(self):
    # test 37
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    prompt_text = "please enter your choice of ant"
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', return_value = "red")
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()

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
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()

  def test_user_can_make_another_choice_if_wrong_input(self):
    # test 40
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    prompt_text = "please enter your choice of ant"
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', side_effect = ["blue", "red"])
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()

  def test_addresses_user_by_name_when_asking_for_ant_choice(self):
    # test 45
    mario = Player("mario")
    allowed_choices = ['red', 'yellow', 'green', 'purple', 'brown']
    prompt_text = "please enter your choice of ant"
    expected_result = "red"
    input_patcher = mock.patch('builtins.input', return_value = "red")
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    input_mock.assert_called_once_with("mario; please enter your choice of ant: ")
    input_patcher.stop()

  def test_returns_user_input_for_input_is_front(self):
    # test 41
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    prompt_text = "please pick a direction to collect food from"
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', return_value = "front")
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()

  def test_returns_user_input_for_input_is_back(self):
    # test 42
    mario = Player("placeholder name")
    allowed_choices = ['front', 'back']
    prompt_text = "please pick a direction to collect food from"
    expected_result = "back"
    input_patcher = mock.patch('builtins.input', return_value = "back")
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()
  
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
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()

  def test_addresses_user_by_name_when_asking_for_direction_choice(self):
    # test 46
    mario = Player("mario")
    allowed_choices = ['front', 'back']
    prompt_text = "please pick a direction to collect food from"
    expected_result = "front"
    input_patcher = mock.patch('builtins.input', return_value = "front")
    input_mock = input_patcher.start()
    mario.make_choice(allowed_choices, prompt_text)
    self.assertEqual(mario.user_choice, expected_result)
    input_mock.assert_called_once_with("mario; please pick a direction to collect food from: ")
    input_patcher.stop()

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
  def test_first_ant_is_red_and_goes_to_top_spot(self):
    # test 32
    mario = Player("mario")
    ant_positions = {"red": 39}
    anthill = [None, None, None, None, None]
    ant = "red"
    expected_new_anthill = [None, None, None, None, "red"]
    expected_new_ant_positions = {"red": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, ant), expected_tuple)

  def test_first_ant_is_green_and_goes_to_top_spot(self):
    # test 33
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, None]
    ant = "green"
    expected_new_anthill = [None, None, None, None, "green"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, ant), expected_tuple)

  def test_top_spot_occupied_second_ant_is_added(self):
    # test 34
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, "red"]
    ant = "green"
    expected_new_anthill = [None, None, None, "green", "red"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, ant), expected_tuple)

  def test_four_spots_occupied_add_fifth_ant(self):
    # test 35
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, "purple", "yellow", "brown", "red"]
    ant = "green"
    expected_new_anthill = ["green", "purple", "yellow", "brown", "red"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, ant), expected_tuple)

  def test_ant_position_is_updated_to_show_it_is_on_anthill(self):
    # test 50
    mario = Player("mario")
    ant_positions = {"green": 39}
    anthill = [None, None, None, None, None]
    ant = "green"
    expected_new_anthill = [None, None, None, None, "green"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.place_ant_on_anthill(ant_positions, anthill, ant), expected_tuple)

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

class MoveAntTest(unittest.TestCase):
  def test_can_use_move_ant_along_trail_for_ants_first_move(self):
    # test 47
    mario = Player("mario")
    trail = ["apple"]
    ant_positions = {"red": None}
    anthill = []
    ant = "red"
    expected_new_ant_positions = {"red": 0}
    expected_tuple = (anthill, expected_new_ant_positions)
    self.assertEqual(mario.move_ant(trail, ant_positions, anthill, ant), expected_tuple)

  def test_can_use_move_ant_along_trail_to_make_typical_move(self):
    # test 48
    mario = Player("mario")
    trail = ["apple", "grapes", "apple"]
    ant_positions = {"red": 0}
    anthill = []
    ant = "red"
    expected_new_ant_positions = {"red": 2}
    expected_tuple = (anthill, expected_new_ant_positions)
    self.assertEqual(mario.move_ant(trail, ant_positions, anthill, ant), expected_tuple)

  def test_can_use_place_ant_on_anthill_to_make_ants_final_move(self):
    # test 49
    mario = Player("mario")
    trail = ["apple", "grapes", "apple"]
    ant_positions = {"red": 0, "purple": 1}
    anthill = [None, None, None, None, None]
    ant = "purple"
    expected_new_anthill = [None, None, None, None, "purple"]
    expected_new_ant_positions = {"red": 0, "purple": "anthill"}
    expected_tuple  = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.move_ant(trail, ant_positions, anthill, ant), expected_tuple)

  def test_ant_moves_from_start_to_anthill_if_none_of_its_food_in_trail(self):
    # test 51
    mario = Player("mario")
    trail = ["apple", "grapes", "cheese", "bread"]
    ant_positions = {"green": None}
    anthill = [None, None, None, None, None]
    ant = "green"
    expected_new_anthill = [None, None, None, None, "green"]
    expected_new_ant_positions = {"green": "anthill"}
    expected_tuple  = (expected_new_anthill, expected_new_ant_positions)
    self.assertEqual(mario.move_ant(trail, ant_positions, anthill, ant), expected_tuple)

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

class TakeTurnTest(unittest.TestCase):
  def test_single_ant_moves_to_centre_of_three_element_trail_picks_front(self):
    # test 66
    # Given
    anthill = [None]
    mario = Player("mario")
    trail = ["pepper", "apple", "cheese"]
    ant_positions = {"red": None}
    input_patcher = mock.patch('builtins.input', side_effect = ["red", "front"])
    input_mock = input_patcher.start()
    # When
    (actual_new_trail, actual_new_ant_positions, actual_new_anthill) = \
      mario.take_turn(trail, ant_positions, anthill)
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

  def test_single_ant_moves_from_centre_of_three_element_trail_onto_anthill(self):
    # test 67
    # Given
    anthill = [None]
    mario = Player("mario")
    mario.hand = {"cheese": 1}
    trail = ["pepper", "apple", None]
    ant_positions = {"red": 1}
    input_patcher = mock.patch('builtins.input', return_value = "red")
    input_mock = input_patcher.start()
    # When
    (actual_new_trail, actual_new_ant_positions, actual_new_anthill) = \
      mario.take_turn(trail, ant_positions, anthill)
    # Then
    expected_new_trail = trail
    expected_new_ant_positions = {"red": "anthill"}
    expected_new_anthill = ["red"]
    self.assertEqual(actual_new_trail, expected_new_trail)
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)
    self.assertEqual(actual_new_anthill, expected_new_anthill)
    self.assertEqual(mario.hand, {"cheese": 1})
    input_patcher.stop()

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

if __name__ == '__main__':
  unittest.main(verbosity = 2)
