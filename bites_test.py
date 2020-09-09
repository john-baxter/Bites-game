import unittest
from constants import ANTS
from constants import TOKENS_FOR_TRAIL
from bites import Bites
from bites import move_ant
from bites import take_food
from bites import place_ant_on_anthill
# from bites import

#TO DO
# class BitesInitTest(unittest.TestCase):

class InitialiseAntsTest(unittest.TestCase):
  # test 1
  def test_can_initialise_one_ant(self):
    ants = ["red"]
    bites_game = Bites(ants, TOKENS_FOR_TRAIL)
    expected_ant_positions = {"red": None}
    self.assertEqual(bites_game.ants, expected_ant_positions)

  def test_can_initialise_two_ants(self):
  # test 2
    ants = ["red", "purple"]
    bites_game = Bites(ants, TOKENS_FOR_TRAIL)
    expected_ant_positions = {"red": None, "purple": None}
    self.assertEqual(bites_game.ants, expected_ant_positions)

  def test_can_initialise_five_ants(self):
  # test 3
    ants = ["red", "purple", "yellow", "green", "brown"]
    bites_game = Bites(ants, TOKENS_FOR_TRAIL)
    expected_ant_positions = {
      "red": None,
      "purple": None,
      "yellow": None,
      "green": None,
      "brown": None,
      }
    self.assertEqual(bites_game.ants, expected_ant_positions)

class InitialiseTrailTest(unittest.TestCase):
  # test 4
  def test_can_initialise_trail_with_one_token(self):
    foods = {"apple": 1}
    bites_game = Bites(ANTS, foods)
    expected_trail = ["apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_initialise_trail_with_two_different_tokens(self):
  # test 5
    foods = {"apple": 1, "grapes": 1}
    bites_game = Bites(ANTS, foods)
    expected_trails = [["apple", "grapes"], ["grapes", "apple"]]
    self.assertIn(bites_game.trail, expected_trails)

  def test_can_initialise_trail_with_five_of_same_token(self):
  # test 6
    foods = {"apple": 5}
    bites_game = Bites(ANTS, foods)
    expected_trail = ["apple", "apple", "apple", "apple", "apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_shuffle_two_plus_one_tokens(self):
  # test 7
    foods = {"apple": 2, "grapes": 1}
    bites_game = Bites(ANTS, foods)
    expected_trails = [
      ["grapes", "apple", "apple"],
      ["apple", "grapes", "apple"],
      ["apple", "apple", "grapes"]
      ]
    self.assertIn(bites_game.trail, expected_trails)

  def test_full_size_trail_using_count_method_and_length(self):
  # test 8
    foods = {
      "apple": 9,
      "grapes": 9,
      "cheese": 9,
      "pepper": 9,
      "bread": 9
    }
    bites_game = Bites(ANTS, foods)
    expected_trail_length = 45
    self.assertEqual(len(bites_game.trail), expected_trail_length)
    self.assertEqual(bites_game.trail.count("apple"), 9)
    self.assertEqual(bites_game.trail.count("grapes"), 9)
    self.assertEqual(bites_game.trail.count("cheese"), 9)
    self.assertEqual(bites_game.trail.count("pepper"), 9)
    self.assertEqual(bites_game.trail.count("bread"), 9)

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

class InitialiseAnthillTest(unittest.TestCase):
  def test_can_initialise_anthill_as_list_with_len_five_and_every_element_is_None(self):
  # test 27
    ants = ['purple', 'red', 'brown', 'yellow', 'green']
    bites_game = Bites(ants, TOKENS_FOR_TRAIL)
    expected_anthill = [None, None, None, None, None]
    self.assertEqual(bites_game.anthill, expected_anthill)

class PlaceAntOnAnthillTest(unittest.TestCase):
  def test_first_ant_is_red_and_goes_to_top_spot(self):
  # test 32
    anthill = [None, None, None, None, None]
    ant = "red"
    expected_new_anthill = [None, None, None, None, "red"]
    actual_new_anthill = place_ant_on_anthill(anthill, ant)
    self.assertEqual(actual_new_anthill, expected_new_anthill)

  def test_first_ant_is_green_and_goes_to_top_spot(self):
  # test 33
    anthill = [None, None, None, None, None]
    ant = "green"
    expected_new_anthill = [None, None, None, None, "green"]
    actual_new_anthill = place_ant_on_anthill(anthill, ant)
    self.assertEqual(actual_new_anthill, expected_new_anthill)

  def test_top_spot_occupied_second_ant_is_added(self):
  # test 34
    anthill = [None, None, None, None, "red"]
    ant = "green"
    expected_new_anthill = [None, None, None, "green", "red"]
    actual_new_anthill = place_ant_on_anthill(anthill, ant)
    self.assertEqual(actual_new_anthill, expected_new_anthill)

  def test_four_spots_occupied_add_fifth_ant(self):
  # test 35
    anthill = [None, "purple", "yellow", "brown", "red"]
    ant = "green"
    expected_new_anthill = ["green", "purple", "yellow", "brown", "red"]
    actual_new_anthill = place_ant_on_anthill(anthill, ant)
    self.assertEqual(actual_new_anthill, expected_new_anthill)



if __name__ == '__main__':
  unittest.main()
