import unittest
from unittest import mock
from unittest.mock import patch, call
from player import Player
from controller import enter_number_of_players
from controller import generate_player
from controller import prepare_list_of_players
from controller import start_new_game
from controller import choose_anthill_rule
from constants import ANTHILL_CARD_DICT

class EnterNumberOfPlayersTest(unittest.TestCase):
  # test 99
  @patch('builtins.input', return_value = 2)
  def test_enter_number_of_players_returns_number_entered(self, mock_builtin_input):
    expected_result = 2
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(mock_builtin_input.call_count, 1)

  @patch('builtins.input', side_effect = ['two', 2])
  @patch('builtins.print')
  def test_enter_number_of_players_does_not_allow_1_player(
    self, mock_builtin_print, mock_builtin_input):
    # test 100
    expected_result = 2
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(mock_builtin_input.call_count, 2)

  @patch('builtins.input', side_effect = ['two', 2])
  @patch('builtins.print')
  def test_enter_number_of_players_does_not_allow_6_players(
    self, mock_builtin_print, mock_builtin_input):
    # test 101
    expected_result = 2
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(mock_builtin_input.call_count, 2)

  @patch('builtins.input', side_effect = ['two', 2])
  @patch('builtins.print')
  def test_check_no_error_if_input_is_not_an_int_player_can_enter_again(
    self, mock_builtin_print, mock_builtin_input):
    # test 102
    expected_result = 2
    actual_result = enter_number_of_players()
    self.assertEqual(actual_result, expected_result)
    self.assertEqual(mock_builtin_input.call_count, 2)

  @patch('builtins.input', return_value = 2)
  def test_user_is_prompted_to_enter_number_of_players(self, mock_builtin_input):
    # test 103
    enter_number_of_players()
    mock_builtin_input.assert_called_once_with("Please enter the number of players: ")

class GeneratePlayerTest(unittest.TestCase):
  @patch('builtins.input', return_value = 'Mario')
  def test_player_name_can_be_entered(self, mock_builtin_input):
    # test 104
    expected_result = generate_player()
    self.assertEqual(expected_result.name, "Mario")
    self.assertEqual(mock_builtin_input.call_count, 1)
    self.assertIsInstance(expected_result, Player)

  @patch('builtins.input', return_value = 'Mario')
  def test_user_is_prompted_to_enter_their_name(self, mock_builtin_input):
    # test 105
    generate_player()
    mock_builtin_input.assert_called_once_with("Please enter your name: ")

class PrepareListOfPlayersTest(unittest.TestCase):
  @patch('builtins.input', return_value = 2)
  def test_prepare_list_of_players_returns_a_list(self, mock_builtin_input):
    # test 106
    actual_result = prepare_list_of_players()
    self.assertIsInstance(actual_result, list)

  @patch('builtins.input', return_value = 2)
  def test_prepare_list_of_players_requests_input_of_number_of_players(
    self, mock_builtin_input):
    # test 107
    prepare_list_of_players()
    self.assertEqual(mock_builtin_input.call_args_list[0], mock.call(
      "Please enter the number of players: "))

  @patch('controller.generate_player')
  @patch('builtins.input', return_value = 2)
  def test_for_2_players_generate_player_is_called_twice(
    self, mock_builtin_input, generate_player_mock):
    # test 108
    prepare_list_of_players()
    self.assertEqual(generate_player_mock.call_count, 2)
    self.assertEqual(mock_builtin_input.call_args_list[0], mock.call(
      "Please enter the number of players: "))

  @patch('controller.generate_player')
  @patch('builtins.input', return_value = 3)
  def test_for_3_players_generate_player_is_called_three_times(
    self, mock_builtin_input, generate_player_mock):
    # test 109
    prepare_list_of_players()
    self.assertEqual(mock_builtin_input.call_args_list[0], mock.call(
      "Please enter the number of players: "))
    self.assertEqual(generate_player_mock.call_count, 3)

class StartNewGameTest(unittest.TestCase):
  @patch('builtins.print')
  @patch('bites.Bites.__init__', return_value = None)
  @patch('bites.Bites.play_full_game')
  @patch('builtins.input', side_effect = [2, 'Mario', 'Luigi', 'top down'])
  def test_start_new_2player_game_calls_prepare_list_of_players_and_associated_functions_in_correct_order_and_with_correct_callcount(
    self, mock_builtin_input, mock_bites_play, mock_bites_init, mock_builtin_print):
    # test 110
    start_new_game()
    self.assertEqual(mock_builtin_input.call_args_list[0], mock.call(
      "Please enter the number of players: "))
    self.assertEqual(mock_builtin_input.call_args_list[1], mock.call(
      "Please enter your name: "))
    self.assertEqual(mock_builtin_input.call_args_list[2], mock.call(
      "Please enter your name: "))
    self.assertGreaterEqual(len(mock_builtin_input.call_args_list), 3)

  @patch('builtins.print')
  @patch('bites.Bites.__init__', return_value = None)
  @patch('bites.Bites.play_full_game')
  @patch('builtins.input', side_effect = [2,'Mario', 'Luigi', 'top down'])
  def test_start_new_game_creates_instance_of_Bites_class(
    self, mock_builtin_input, mock_bites_play, mock_bites_init, mock_builtin_print):
    # test 111
    start_new_game()
    self.assertEqual(mock_bites_init.call_count, 1)

  @patch('builtins.print')
  @patch('bites.Bites.__init__', return_value = None)
  @patch('bites.Bites.play_full_game')
  @patch('builtins.input', side_effect = [2,'Mario', 'Luigi', 'top down'])
  def test_start_new_game_calls_Bites_play_full_game_method(
    self, mock_builtin_input, mock_bites_play, mock_bites_init, mock_builtin_print):
    # test 112
    start_new_game()
    mock_bites_play.assert_called_once()

class ChooseAnthillRuleTest(unittest.TestCase):
  @patch('builtins.input', return_value = "top down")
  @patch('builtins.print')
  def test_choose_anthill_rule_allows_choice_of_top_down_option(
    self, mock_builtin_print, mock_builtin_input):
    # test 137
    expected_result = "top down"
    self.assertEqual(choose_anthill_rule(), expected_result)

  @patch('builtins.input', return_value = "bottom up")
  @patch('builtins.print')
  def test_choose_anthill_rule_allows_choice_of_bottom_up(
    self, mock_builtin_print, mock_builtin_input):
    # test 138
    expected_result = "bottom up"
    self.assertEqual(choose_anthill_rule(), expected_result)

  @patch('builtins.input', return_value = "leave gaps")
  @patch('builtins.print')
  def test_choose_anthill_rule_allows_choice_of_leave_gaps(
    self, mock_builtin_print, mock_builtin_input):
    # test 139
    expected_result = "leave gaps"
    self.assertEqual(choose_anthill_rule(), expected_result)

  @patch('builtins.input', side_effect = ["top up", "bottom up"])
  @patch('builtins.print')
  def test_user_makes_typo_no_error_redo_choice_select_botom_up(
    self, mock_builtin_print, mock_builtin_input):
    # test 140
    expected_result = "bottom up"
    self.assertEqual(choose_anthill_rule(), expected_result)

  @patch('builtins.input', return_value = "random")
  @patch('builtins.print')
  def test_user_can_enter_random_and_one_of_the_other_options_is_selected(
    self, mock_builtin_print, mock_builtin_input):
    # test 143
    expected_results = ["top down", "bottom up", "leave gaps", "user choice"]
    self.assertIn(choose_anthill_rule(), expected_results)

  @patch('builtins.input', return_value = "top down")
  @patch('builtins.print')
  def test_choose_anthill_rule_displays_available_options_and_prompt_text(
    self, mock_builtin_print, mock_builtin_input):
    # test 144
    choose_anthill_rule()
    expected_print_result_0 = call("\nThe available options are:")
    expected_print_result_1 = call("top down")
    expected_print_result_2 = call("bottom up")
    expected_print_result_3 = call("leave gaps")
    expected_print_result_5 = call("Or enter 'random' to select one of the above options")
    expected_input_result = call("Please enter your choice of anthill card: ")
    self.assertEqual(mock_builtin_print.call_args_list[0], expected_print_result_0)
    self.assertEqual(mock_builtin_print.call_args_list[1], expected_print_result_1)
    self.assertEqual(mock_builtin_print.call_args_list[2], expected_print_result_2)
    self.assertEqual(mock_builtin_print.call_args_list[3], expected_print_result_3)
    self.assertEqual(mock_builtin_print.call_args_list[5], expected_print_result_5)
    self.assertEqual(mock_builtin_input.call_args_list[0], expected_input_result)

  @patch('builtins.input', return_value = "user choice")
  @patch('builtins.print')
  def test_choose_anthill_rule_also_displays_user_choice_option_and_allows_it_to_be_selected(
    self, mock_builtin_print, mock_builtin_input):
    # test 151
    expected_print_result_3 = call("leave gaps")
    expected_print_result_4 = call("user choice")
    expected_print_result_5 = call("Or enter 'random' to select one of the above options")
    expected_returned_choice = "user choice"
    actual_returned_choice = choose_anthill_rule()
    self.assertEqual(mock_builtin_print.call_args_list[3], expected_print_result_3)
    self.assertEqual(mock_builtin_print.call_args_list[4], expected_print_result_4)
    self.assertEqual(mock_builtin_print.call_args_list[5], expected_print_result_5)
    self.assertEqual(actual_returned_choice, expected_returned_choice)

if __name__ == '__main__':
  unittest.main(verbosity = 2)
