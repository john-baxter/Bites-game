import unittest
from bites import initialise_ants
from bites import initialise_path

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

class InitialisePathTest(unittest.TestCase):
  # test 4
  def test_can_initialise_path_with_one_token(self):
    foods = {"apple": 1}
    expected_path = ["apple"]
    actual_path = initialise_path(foods)
    self.assertEqual(expected_path, actual_path)

  def test_can_initialise_path_with_two_different_tokens(self):
  # test 5
    foods = {"apple": 1, "grapes": 1}
    expected_paths = [["apple", "grapes"], ["grapes", "apple"]]
    actual_path = initialise_path(foods)
    self.assertIn(actual_path, expected_paths)

  def test_can_initialise_path_with_five_of_same_token(self):
  # test 6
    foods = {"apple": 5}
    expected_path = ["apple", "apple", "apple", "apple", "apple"]
    actual_path = initialise_path(foods)
    self.assertEqual(expected_path, actual_path)

  def test_can_shuffle_two_plus_one_tokens(self):
  # test 7
    foods = {"apple": 2, "grapes": 1}
    expected_paths = [
      ["grapes", "apple", "apple"],
      ["apple", "grapes", "apple"],
      ["apple", "apple", "grapes"]
      ]
    actual_path = initialise_path(foods)
    self.assertIn(actual_path, expected_paths)

  def test_full_size_path_using_count_method_and_length(self):
  # test 7
    foods = {
      "apple": 10,
      "grapes": 10,
      "cheese": 10,
      "pepper": 10,
      "bread": 10
    }
    expected_path_length = 50
    path = initialise_path(foods)
    actual_path_length = len(path)
    self.assertEqual(actual_path_length, expected_path_length)
    self.assertEqual(path.count("apple"), 1)
    self.assertEqual(path.count("grapes"), 1)
    self.assertEqual(path.count("cheese"), 10)
    self.assertEqual(path.count("pepper"), 10)
    self.assertEqual(path.count("bread"), 10)





if __name__ == '__main__':
  unittest.main()
