import unittest
from bites import initialise_ants
from bites import initialise_trail
from bites import initialise_hand
from bites import move_ant
from bites import take_food
from bites import store_food
from bites import score_hand
from bites import initialise_anthill
# from bites import

class InitialiseAntsTest(unittest.TestCase):
  # test 1
  def test_can_initialise_one_ant(self):
    ants = ["red"]
    expected_ant_positions = {"red": None}
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

  def test_can_initialise_two_ants(self):
  # test 2
    ants = ["red", "purple"]
    expected_ant_positions = {"red": None, "purple": None}
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

  def test_can_initialise_five_ants(self):
  # test 3
    ants = ["red", "purple", "yellow", "green", "brown"]
    expected_ant_positions = {
      "red": None,
      "purple": None,
      "yellow": None,
      "green": None,
      "brown": None,
      }
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

class InitialiseTrailTest(unittest.TestCase):
  # test 4
  def test_can_initialise_trail_with_one_token(self):
    foods = {"apple": 1}
    expected_trail = ["apple"]
    actual_trail = initialise_trail(foods)
    self.assertEqual(expected_trail, actual_trail)

  def test_can_initialise_trail_with_two_different_tokens(self):
  # test 5
    foods = {"apple": 1, "grapes": 1}
    expected_trails = [["apple", "grapes"], ["grapes", "apple"]]
    actual_trail = initialise_trail(foods)
    self.assertIn(actual_trail, expected_trails)

  def test_can_initialise_trail_with_five_of_same_token(self):
  # test 6
    foods = {"apple": 5}
    expected_trail = ["apple", "apple", "apple", "apple", "apple"]
    actual_trail = initialise_trail(foods)
    self.assertEqual(expected_trail, actual_trail)

  def test_can_shuffle_two_plus_one_tokens(self):
  # test 7
    foods = {"apple": 2, "grapes": 1}
    expected_trails = [
      ["grapes", "apple", "apple"],
      ["apple", "grapes", "apple"],
      ["apple", "apple", "grapes"]
      ]
    actual_trail = initialise_trail(foods)
    self.assertIn(actual_trail, expected_trails)

  def test_full_size_trail_using_count_method_and_length(self):
  # test 8
    foods = {
      "apple": 10,
      "grapes": 10,
      "cheese": 10,
      "pepper": 10,
      "bread": 10
    }
    expected_trail_length = 50
    trail = initialise_trail(foods)
    actual_trail_length = len(trail)
    self.assertEqual(actual_trail_length, expected_trail_length)
    self.assertEqual(trail.count("apple"), 10)
    self.assertEqual(trail.count("grapes"), 10)
    self.assertEqual(trail.count("cheese"), 10)
    self.assertEqual(trail.count("pepper"), 10)
    self.assertEqual(trail.count("bread"), 10)

# class InitialiseHandTest(unittest.TestCase):
#   def test_can_initialise_player_hand(self):
#   # test 9
#     hand = initialise_hand()
#     self.assertIsInstance(hand, dict)
#     self.assertEqual(len(hand), 0)

class MoveAntTest(unittest.TestCase):
  def test_can_move_onto_trail_of_length_one(self):
  # test 10
    ant_positions = {"red": None}
    trail = ["apple"]
    expected_new_ant_positions = {"red": 0}
    actual_new_ant_positions = move_ant(trail, ant_positions, "red")
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)

  def test_can_move_onto_adjacent_position(self):
  # test 11
    ant_positions = {"red": 0}
    trail = ["apple", "apple"]
    expected_new_ant_positions = {"red": 1}
    actual_new_ant_positions = move_ant(trail, ant_positions, "red")
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)

  def test_ant_moves_past_wrong_food_tokens(self):
  # test 12
    ant_positions = {"red": 0}
    trail = ["apple", "grapes", "apple"]
    expected_new_ant_positions = {"red": 2}
    actual_new_ant_positions = move_ant(trail, ant_positions, "red")
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)

  def test_ant_moves_past_missing_food_tokens(self):
  # test 13
    ant_positions = {"red": 0}
    trail = ["apple", None, "apple"]
    expected_new_ant_positions = {"red": 2}
    actual_new_ant_positions = move_ant(trail, ant_positions, "red")
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)

  def test_only_intended_ant_moves(self):
  # test 14
    ant_positions = {"red": 0, "purple": 1}
    trail = ["apple", "grapes", "apple"]
    expected_new_ant_positions = {"red": 2, "purple": 1}
    actual_new_ant_positions = move_ant(trail, ant_positions, "red")
    self.assertEqual(actual_new_ant_positions, expected_new_ant_positions)

class TakeFoodTest(unittest.TestCase):
  def test_single_ant_on_trail_can_take_food_in_front(self):
  # test 15
    trail = ["apple", "grapes", "cheese"]
    ant_positions = {"purple": 1}
    ant = "purple"
    direction = "front"
    expected_food = "cheese"
    expected_new_trail = ["apple", "grapes", None]
    (actual_food, actual_new_trail) = take_food(trail, ant_positions, ant, direction)
    self.assertEqual(actual_food, expected_food)
    self.assertEqual(actual_new_trail, expected_new_trail)

  def test_single_ant_on_trail_can_take_food_behind(self):
  # test 16
    trail = ["apple", "grapes", "cheese"]
    ant_positions = {"purple": 1}
    ant = "purple"
    direction = "back"
    expected_food = "apple"
    expected_new_trail = [None, "grapes", "cheese"]
    (actual_food, actual_new_trail) = take_food(trail, ant_positions, ant, direction)
    self.assertEqual(actual_food, expected_food)
    self.assertEqual(actual_new_trail, expected_new_trail)

  def test_adjacent_food_is_blocked_by_presence_of_other_ant(self):
  # test 17
    trail = ["apple", "grapes", "cheese", "bread"]
    ant_positions = {"purple": 1, "yellow": 2}
    ant = "purple"
    direction = "front"
    expected_food = "bread"
    expected_new_trail = ["apple", "grapes", "cheese", None]
    (actual_food, actual_new_trail) = take_food(trail, ant_positions, ant, direction)
    self.assertEqual(actual_food, expected_food)
    self.assertEqual(actual_new_trail, expected_new_trail)

  def test_raises_value_error_if_direction_is_wrong(self):
  # test 18
    trail = ["apple", "grapes", "cheese", "bread"]
    ant_positions = {"purple": 1, "yellow": 2}
    ant = "purple"
    direction = "forwards"
    self.assertRaises(ValueError, take_food, trail, ant_positions, ant, direction)

class StoreFoodTest(unittest.TestCase):
  # def test_can_receive_single_food_to_empty_hand(self):
  # # test 19
  #   hand = {}
  #   food = "apple"
  #   expected_new_hand = {"apple": 1}
  #   actual_new_hand = store_food(hand, food)
  #   self.assertEqual(actual_new_hand, expected_new_hand)

  # def test_can_receive_second_token_of_same_food(self):
  # # test 20
  #   hand = {"apple": 1}
  #   food = "apple"
  #   expected_new_hand = {"apple": 2}
  #   actual_new_hand = store_food(hand, food)
  #   self.assertEqual(actual_new_hand, expected_new_hand)

  def test_can_receive_food_not_already_in_hand(self):
  # test 21
    hand = {"apple": 2}
    food = "cheese"
    expected_new_hand = {"apple": 2, "cheese": 1}
    actual_new_hand = store_food(hand, food)
    self.assertEqual(actual_new_hand, expected_new_hand)

class ScoreHandTest(unittest.TestCase):
  def test_can_score_four_points_for_one_token_in_top_slot(self):
  # test 22
    anthill = ["red", "purple", "yellow", "brown", "green"]
    hand = {"pepper": 1}
    expected_score = 4
    actual_score = score_hand(hand, anthill)
    self.assertEqual(actual_score, expected_score)

  def test_can_score_three_points_for_one_token_in_second_top_slot(self):
  # test 23
    anthill = ["red", "purple", "yellow", "brown", "green"]
    hand = {"bread": 1}
    expected_score = 3
    actual_score = score_hand(hand, anthill)
    self.assertEqual(actual_score, expected_score)

  def test_can_score_four_points_for_two_tokens_in_middle_slot(self):
  # test 24
    anthill = ["red", "purple", "yellow", "brown", "green"]
    hand = {"cheese": 2}
    expected_score = 4
    actual_score = score_hand(hand, anthill)
    self.assertEqual(actual_score, expected_score)

  def test_can_score_ten_points_for_one_of_each_token(self):
  # test 25
    anthill = ["red", "purple", "yellow", "brown", "green"]
    hand = {
      "apple": 1,
      "grapes": 1,
      "cheese": 1,
      "bread": 1,
      "pepper": 1}
    expected_score = 10
    actual_score = score_hand(hand, anthill)
    self.assertEqual(actual_score, expected_score)

  def test_can_score_twenty_points_for_two_of_each_token(self):
  # test 26
    anthill = ["red", "purple", "yellow", "brown", "green"]
    hand = {
      "apple": 2,
      "grapes": 2,
      "cheese": 2,
      "bread": 2,
      "pepper": 2}
    expected_score = 20
    actual_score = score_hand(hand, anthill)
    self.assertEqual(actual_score, expected_score)

class InitialiseAnthillTest(unittest.TestCase):
  def test_can_initialise_anthill_as_list_with_len_five_and_every_element_is_None(self):
  # test 27  
    expected_anthill = [None, None, None, None, None]
    actual_anthill = initialise_anthill()
    self.assertEqual(actual_anthill, expected_anthill)

class PlaceAntOnAnthillTest(unittest.TestCase):
  def test_first_ant_goes_to_top_spot(self):


  






if __name__ == '__main__':
  unittest.main()
