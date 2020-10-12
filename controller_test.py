import unittest
from unittest import mock
from unittest.mock import patch
from player import Player
from controller import enter_number_of_players
from controller import generate_player
from controller import prepare_list_of_players
from controller import start_new_game

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
    input_patcher.stop()

class GeneratePlayerTest(unittest.TestCase):
  def test_player_name_can_be_entered(self):
    # test 104
    input_patcher = mock.patch('builtins.input', return_value = "Mario")
    input_mock = input_patcher.start()
    expected_result = generate_player()
    self.assertEqual(expected_result.name, "Mario")
    self.assertEqual(input_mock.call_count, 1)
    self.assertIsInstance(expected_result, Player)
    input_patcher.stop()

  def test_user_is_prompted_to_enter_their_name(self):
    # test 105
    input_patcher = mock.patch('builtins.input', return_value = "Mario")
    input_mock = input_patcher.start()
    generate_player()
    input_mock.assert_called_once_with("Please enter your name: ")
    input_patcher.stop()

class PrepareListOfPlayersTest(unittest.TestCase):
  def test_prepare_list_of_players_returns_a_list(self):
    # test 106
    input_patcher = mock.patch('builtins.input', return_value = 2)
    input_mock = input_patcher.start()
    actual_result = prepare_list_of_players()
    self.assertIsInstance(actual_result, list)
    input_patcher.stop()

  def test_prepare_list_of_players_requests_input_of_number_of_players(self):
    # test 107
    input_patcher = mock.patch('builtins.input', return_value = 2)
    input_mock = input_patcher.start()
    prepare_list_of_players()
    self.assertEqual(input_mock.call_args_list[0], mock.call(
      "Please enter the number of players: "))
    input_patcher.stop()

  @patch('controller.generate_player')
  def test_for_2_players_generate_player_is_called_twice(
    self, generate_player_mock):
    # test 108
    manager = mock.Mock()
    manager.attach_mock(generate_player_mock, 'generate_player')
    input_patcher = mock.patch('builtins.input', return_value = 2)
    input_mock = input_patcher.start()
    prepare_list_of_players()
    self.assertEqual(generate_player_mock.call_count, 2)
    self.assertEqual(input_mock.call_args_list[0], mock.call(
      "Please enter the number of players: "))
    input_patcher.stop()

  @patch('controller.generate_player')
  def test_for_3_players_generate_player_is_called_three_times(
    self, generate_player_mock):
    # test 109
    manager = mock.Mock()
    manager.attach_mock(generate_player_mock, 'generate_player')
    input_patcher = mock.patch('builtins.input', return_value = 3)
    input_mock = input_patcher.start()
    prepare_list_of_players()
    self.assertEqual(input_mock.call_args_list[0], mock.call(
      "Please enter the number of players: "))
    self.assertEqual(generate_player_mock.call_count, 3)
    input_patcher.stop()

class StartNewGameTest(unittest.TestCase):
  def test_start_new_2player_game_calls_prepare_list_of_players_and_associated_functions_in_correct_order_and_with_correct_callcount(
    self):
    # test 110
    input_patcher = mock.patch('builtins.input', side_effect = [2, "Mario", "Luigi"])
    input_mock = input_patcher.start()
    start_new_game()
    self.assertEqual(input_mock.call_args_list[0], mock.call(
      "Please enter the number of players: "))
    self.assertEqual(input_mock.call_args_list[1], mock.call(
      "Please enter your name: "))
    self.assertEqual(input_mock.call_args_list[2], mock.call(
      "Please enter your name: "))
    self.assertEqual(len(input_mock.call_args_list), 3)
    input_patcher.stop()

  @patch('bites.Bites')
  def test_start_new_game_creates_instance_of_Bites_class(self, mock_bites_init):
    # test 111
    manager = mock.Mock()
    mock_bites_init.return_value = None
    input_patcher = mock.patch('builtins.input', return_value = 2)
    input_mock = input_patcher.start()
    mock_bites_init.assert_called





if __name__ == '__main__':
  unittest.main(verbosity = 2)
