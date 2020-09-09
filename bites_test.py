import unittest
from bites import initialise_ants
from bites import initialise_trail
from bites import move_ant
from bites import take_food
from bites import initialise_anthill
from bites import place_ant_on_anthill
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
    expected_anthill = [None, None, None, None, None]
    actual_anthill = initialise_anthill(ants)
    self.assertEqual(actual_anthill, expected_anthill)

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
