import unittest
from unittest import mock
from controller import enter_number_of_players

class GetPlayerInfoTest(unittest.TestCase):
  # test 99
  def test_enter_number_of_players_returns_number_entered(self):
    expected_result = 2
    input_patcher = mock.patch('builtins.input', return_value = 2)
    input_mock = input_patcher.start()
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(input_mock.call_count, 1)
    input_patcher.stop()

  def test_enter_number_of_players_does_not_allow_1_player(self):
    # test 100
    expected_result = 2
    input_patcher = mock.patch('builtins.input', side_effect = [1, 2])
    input_mock = input_patcher.start()
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()

  def test_enter_number_of_players_does_not_allow_6_players(self):
    # test 101
    expected_result = 2
    input_patcher = mock.patch('builtins.input', side_effect = [6, 2])
    input_mock = input_patcher.start()
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()

  def test_check_no_error_if_input_is_not_an_int_player_can_enter_again(self):
    # test 102
    expected_result = 2
    input_patcher = mock.patch('builtins.input', side_effect = ["two", 2])
    input_mock = input_patcher.start()
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(input_mock.call_count, 2)
    input_patcher.stop()

  def test_user_is_prompted_to_enter_number_of_players(self):
    # test 103
    input_patcher = mock.patch('builtins.input', return_value = 2)
    input_mock = input_patcher.start()
    enter_number_of_players()
    input_mock.assert_called_once_with("Please enter the number of players: ")








if __name__ == '__main__':
  unittest.main(verbosity = 2)
