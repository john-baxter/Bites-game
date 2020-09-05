import unittest
from bites import initialise_ants

class InitialiseAntsTest(unittest.TestCase):
  def test_can_initialise_one_ant(self):
    ants = ["red"]
    expected_ant_positions = {"red": None}
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

  def test_can_initialise_two_ants(self):
    ants = ["red", "blue"]
    expected_ant_positions = {"red": None, "blue": None}
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

  def test_can_initialise_five_ants(self):
    ants = ["red", "blue", "yellow", "green", "brown"]
    expected_ant_positions = {
      "red": None,
      "blue": None,
      "yellow": None,
      "green": None,
      "brown": None,
      }
    actual_ant_positions = initialise_ants(ants)
    self.assertEqual(expected_ant_positions, actual_ant_positions)

if __name__ == '__main__':
  unittest.main()
