import unittest
from unittest import mock
import controller

class GetPlayerInfoTest(unittest.TestCase):
  # test 99
  def test_enter_number_of_players_returns_number_entered(self):
    expected_result = 2
    input_patcher = mock.patch('builtins.input', return_value = 2)
    input_mock = input_patcher.start()
    actual_result = controller.enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()

  def test_enter_number_of_players_does_not_allow_1_player(self):
    # test 100
    expected_result = 2
    input_patcher = mock.patch('builtins.input', side_effect = [1, 2])
    input_mock = input_patcher.start()
    actual_result = controller.enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()










if __name__ == '__main__':
  unittest.main(verbosity = 2)
