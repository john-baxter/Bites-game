import unittest
from bites import initialise_ants
from bites import initialise_path

class InitialiseAntsTest(unittest.TestCase):
  def test_can_initialise_one_ant(self):
    ants = ["red"]
    expected_ant_positions = {"red": None}
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

  def test_can_initialise_two_ants(self):
    ants = ["red", "purple"]
    expected_ant_positions = {"red": None, "purple": None}
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

  def test_can_initialise_five_ants(self):
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
  def test_can_initialise_path_with_one_token(self):
    foods = {"apple": 1}
    expected_path_length = 1
    # expected_path_tokens
    actual_path = initialise_path(foods)
    actual_path_length = len(actual_path)
    self.assertEqual(expected_path_length, actual_path_length)


if __name__ == '__main__':
  unittest.main()
