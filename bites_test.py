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





if __name__ == '__main__':
  unittest.main()
