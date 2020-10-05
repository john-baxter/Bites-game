import unittest
from unittest import mock
from unittest.mock import patch
from bites import Bites

class BitesInitTest(unittest.TestCase):
  def test___init___method_works(self):
    # test 36
    # This test was written rertrospectively; the __init__ method came about 
    # naturally during refactoring of the code into the Bites class.
    test_ants = ['purple', 'yellow']
    test_tokens = {
      'grapes': 1,
      'cheese': 1}
    test_players = []
    bites_game = Bites(test_ants, test_tokens, test_players)
    expected_ants = {
      'purple': None,
      'yellow': None}
    expected_trails = [
      ['grapes', 'cheese'],
      ['cheese', 'grapes']]
    expected_anthill = [None, None]
    self.assertIsInstance(bites_game, Bites)
    self.assertEqual(bites_game.ant_positions, expected_ants)
    self.assertIn(bites_game.trail, expected_trails)
    self.assertEqual(bites_game.anthill, expected_anthill)

  def test_bites_class_can_receive_instance_of_player_class(self):
    # test 73
    class FakePlayer():
      pass

    mario = FakePlayer()
    ants = []
    tokens_for_trail = {}
    bites_game = Bites(ants, tokens_for_trail, [mario])
    self.assertIsInstance(bites_game.players[0], FakePlayer)

  def test_bites_class_can_receive_two_instances_of_player(self):
    # test 74
    class FakePlayer():
      def __init__(self, name):
        self.name = name

    mario = FakePlayer("mario")
    luigi = FakePlayer("luigi")
    players = [mario, luigi]
    ants = []
    tokens_for_trail = {}
    bites_game = Bites(ants, tokens_for_trail, players)
    self.assertEqual(len(bites_game.players), 2)
    self.assertEqual(bites_game.players[0].name, "mario")
    self.assertEqual(bites_game.players[1].name, "luigi")

class InitialiseAntsTest(unittest.TestCase):
  def test_can_initialise_one_ant(self):
    # test 1
    ants = ["red"]
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    expected_ant_positions = {"red": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_two_ants(self):
    # test 2
    ants = ["red", "purple"]
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    expected_ant_positions = {"red": None, "purple": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_five_ants(self):
    # test 3
    ants = ["red", "purple", "yellow", "green", "brown"]
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    expected_ant_positions = {
      "red": None,
      "purple": None,
      "yellow": None,
      "green": None,
      "brown": None,}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

class InitialiseTrailTest(unittest.TestCase):
  def test_can_initialise_trail_with_one_token(self):
    # test 4
    foods = {"apple": 1}
    ants = []
    players = []
    bites_game = Bites(ants, foods, players)
    expected_trail = ["apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_initialise_trail_with_two_different_tokens(self):
    # test 5
    foods = {"apple": 1, "grapes": 1}
    ants = []
    players = []
    bites_game = Bites(ants, foods, players)
    expected_trails = [["apple", "grapes"], ["grapes", "apple"]]
    self.assertIn(bites_game.trail, expected_trails)

  def test_can_initialise_trail_with_five_of_same_token(self):
    # test 6
    foods = {"apple": 5}
    ants = []
    players = []
    bites_game = Bites(ants, foods, players)
    expected_trail = ["apple", "apple", "apple", "apple", "apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_shuffle_two_plus_one_tokens(self):
    # test 7
    foods = {"apple": 2, "grapes": 1}
    ants = []
    players = []
    bites_game = Bites(ants, foods, players)
    expected_trails = [
      ["grapes", "apple", "apple"],
      ["apple", "grapes", "apple"],
      ["apple", "apple", "grapes"]]
    self.assertIn(bites_game.trail, expected_trails)

  def test_full_size_trail_using_count_method_and_length(self):
    # test 8
    foods = {
      "apple": 9,
      "grapes": 9,
      "cheese": 9,
      "pepper": 9,
      "bread": 9}
    ants = []
    players = []
    bites_game = Bites(ants, foods, players)
    expected_trail_length = 45
    self.assertEqual(len(bites_game.trail), expected_trail_length)
    self.assertEqual(bites_game.trail.count("apple"), 9)
    self.assertEqual(bites_game.trail.count("grapes"), 9)
    self.assertEqual(bites_game.trail.count("cheese"), 9)
    self.assertEqual(bites_game.trail.count("pepper"), 9)
    self.assertEqual(bites_game.trail.count("bread"), 9)

class InitialiseAnthillTest(unittest.TestCase):
  def test_can_initialise_anthill_as_list_with_len_five_and_every_element_is_None(self):
    # test 27
    ants = ['purple', 'red', 'brown', 'yellow', 'green']
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    expected_anthill = [None, None, None, None, None]
    self.assertEqual(bites_game.anthill, expected_anthill)

class TakeAllTurnsTest(unittest.TestCase):
  def test_first_player_takes_one_turn(self):
    # test 75
    starting_trail = ["apple", "apple"]
    starting_ant_positions = {
      "red": None,
      "yellow": None,
      "green": None,
      "brown": None,
      "purple": None}
    starting_anthill = [None, None, None, None, None]
    
    trail_after_turn_1_mario = ["apple", None]
    ant_pos_after_turn_1_mario = {
      "red": 0,
      "yellow": None,
      "green": None,
      "brown": None,
      "purple": None}
    anthill_after_turn_1_mario = starting_anthill

    expected_new_trail = trail_after_turn_1_mario
    expected_new_ant_positions = ant_pos_after_turn_1_mario
    expected_new_anthill = starting_anthill
    
    fake_mario = mock.MagicMock()
    fake_mario.take_turn = mock.MagicMock(side_effect = [(
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario),
      ([], {}, [])])
    
    ants = ["red", "yellow", "green", "brown", "purple"]
    tokens_for_trail = {}
    players = [fake_mario]
    bites_game = Bites(ants, tokens_for_trail, players)

    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill

    bites_game.take_all_turns()

    self.assertGreaterEqual(fake_mario.take_turn.call_count, 1)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill))
  
  def test_one_whole_round_is_played(self):
    # test 76
    """
    P0 moves brown ant to pos 2 & picks up cheese from behind
    P1 moves yellow ant to pos 6 & picks up apple from behind
    """
    starting_trail = [
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes", 
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes"]
    starting_ant_positions = {
      "red": None,
      "yellow": None,
      "green": None,
      "brown": None,
      "purple": None}
    starting_anthill = [None, None, None, None, None]
    
    trail_after_turn_1_mario = [
      "apple", 
      None, 
      "bread", 
      "pepper", 
      "grapes", 
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes"]
    ant_pos_after_turn_1_mario = {
      "red": None,
      "yellow": None,
      "green": None,
      "brown": 2,
      "purple": None}
    anthill_after_turn_1_mario = starting_anthill
    fake_mario = mock.MagicMock()
    fake_mario.take_turn = mock.MagicMock(side_effect = [(
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario),
      ([], {}, [])])
    
    trail_after_turn_2_luigi = [
      "apple", 
      None, 
      "bread", 
      "pepper", 
      "grapes", 
      None, 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes"]
    ant_pos_after_turn_2_luigi = {
      "red": None,
      "yellow": 6,
      "green": None,
      "brown": 2,
      "purple": None}
    anthill_after_turn_2_luigi = starting_anthill
    fake_luigi = mock.MagicMock()
    fake_luigi.take_turn = mock.MagicMock(return_value = (
      trail_after_turn_2_luigi, ant_pos_after_turn_2_luigi, anthill_after_turn_2_luigi))
    
    ants = ["red", "yellow", "green", "brown", "purple"]
    tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, tokens_for_trail, players)
    
    expected_new_trail = trail_after_turn_2_luigi
    expected_new_ant_positions = ant_pos_after_turn_2_luigi
    expected_new_anthill = starting_anthill

    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill
    
    bites_game.take_all_turns()
    
    self.assertGreaterEqual(fake_mario.take_turn.call_count, 1)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill))
    self.assertGreaterEqual(fake_luigi.take_turn.call_count, 1)
    self.assertEqual(fake_luigi.take_turn.call_args_list[0], mock.call(
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario))

  def test_two_full_rounds_are_played(self):
    # test 77
    """
    P0 moves green ant to pos 3 & picks up grapes from front
    P1 moves brown ant to pos 2 & picks up apple from front
    P0 moves brown ant to pos 7 & picks up cheese from back
    P1 moves yellow ant to pos 1 & picks up bread from front
    """
    starting_trail = [
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes", 
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes"]
    starting_ant_positions = {
      "red": None,
      "yellow": None,
      "green": None,
      "brown": None,
      "purple": None}
    starting_anthill = [
      None, None, None, None, None]

    trail_after_turn_1_mario = [
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      None, 
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes"]
    ant_pos_after_turn_1_mario = {
      "red": None,
      "yellow": None,
      "green": 3,
      "brown": None,
      "purple": None}
    anthill_after_turn_1_mario = starting_anthill
    
    trail_after_turn_2_luigi = [
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      None, 
      None, 
      "cheese", 
      "bread", 
      "pepper", 
      "grapes"]
    ant_pos_after_turn_2_luigi = {
      "red": None,
      "yellow": None,
      "green": 3,
      "brown": 2,
      "purple": None}
    anthill_after_turn_2_luigi = starting_anthill

    trail_after_turn_3_mario = [
      "apple", 
      "cheese", 
      "bread", 
      "pepper", 
      None, 
      None, 
      None, 
      "bread", 
      "pepper", 
      "grapes"]
    ant_pos_after_turn_3_mario = {
      "red": None,
      "yellow": None,
      "green": 3,
      "brown": 7,
      "purple": None}
    anthill_after_turn_3_mario = starting_anthill
    
    trail_after_turn_4_luigi = [
      "apple", 
      "cheese", 
      None, 
      "pepper", 
      None, 
      None, 
      None, 
      "bread", 
      "pepper", 
      "grapes"]
    ant_pos_after_turn_4_luigi = {
      "red": None,
      "yellow": 1,
      "green": 3,
      "brown": 7,
      "purple": None}
    anthill_after_turn_4_luigi = starting_anthill

    expected_new_trail = trail_after_turn_4_luigi 
    expected_new_ant_positions = ant_pos_after_turn_4_luigi
    expected_new_anthill = anthill_after_turn_4_luigi

    ants = ["red", "yellow", "green", "brown", "purple"]
    tokens_for_trail = {}
    
    fake_mario = mock.MagicMock()
    fake_mario.take_turn = mock.MagicMock(side_effect = [
      (trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario),
      (trail_after_turn_3_mario, ant_pos_after_turn_3_mario, anthill_after_turn_3_mario),
      ([], {}, [])])

    fake_luigi = mock.MagicMock()
    fake_luigi.take_turn = mock.MagicMock(side_effect = [
      (trail_after_turn_2_luigi, ant_pos_after_turn_2_luigi, anthill_after_turn_2_luigi),
      (trail_after_turn_4_luigi, ant_pos_after_turn_4_luigi, anthill_after_turn_4_luigi)])
    
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill
    bites_game.take_all_turns()
    
    self.assertGreaterEqual(fake_mario.take_turn.call_count, 2)
    self.assertEqual(fake_luigi.take_turn.call_count, 2)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill))
    self.assertEqual(fake_luigi.take_turn.call_args_list[0], mock.call(
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario))
    self.assertEqual(fake_mario.take_turn.call_args_list[1], mock.call(
      trail_after_turn_2_luigi, ant_pos_after_turn_2_luigi, anthill_after_turn_2_luigi))
    self.assertEqual(fake_luigi.take_turn.call_args_list[1], mock.call(
      trail_after_turn_3_mario, ant_pos_after_turn_3_mario, anthill_after_turn_3_mario))

  def test_the_game_is_played_until_all_ants_are_on_the_anthill(self):
    # test 78
    """
    The final move of a game;
    P0 moves purple ant to anthill[0]
    """
    starting_trail = [
      "apple",
      None,
      None,
      "pepper",
      None,
      None,
      None,
      "bread",
      "pepper",
      None]
    starting_ant_positions = {
      "purple": None,
      "brown": "anthill",
      "green": "anthill",
      "red": "anthill",
      "yellow": "anthill"}
    starting_anthill = [None, "brown", "green", "red", "yellow"]

    trail_after_turn_1_mario = starting_trail
    ant_pos_after_turn_1_mario = {
      "purple": "anthill",
      "brown": "anthill",
      "green": "anthill",
      "red": "anthill",
      "yellow": "anthill"}
    anthill_after_turn_1_mario = ["purple", "brown", "green", "red", "yellow"]

    expected_new_trail = trail_after_turn_1_mario
    expected_new_ant_positions = ant_pos_after_turn_1_mario
    expected_new_anthill = anthill_after_turn_1_mario

    ants = ["red", "yellow", "green", "brown", "purple"]
    tokens_for_trail = {}
    
    fake_mario = mock.MagicMock()
    fake_mario.take_turn = mock.MagicMock(return_value = (
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario))

    players = [fake_mario]
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill
    bites_game.take_all_turns()

    self.assertEqual(fake_mario.take_turn.call_count, 1)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill))
    self.assertEqual(bites_game.trail, expected_new_trail)
    self.assertEqual(bites_game.ant_positions, expected_new_ant_positions)
    self.assertEqual(bites_game.anthill, expected_new_anthill)

  def test_final_scores_are_printed_at_the_end_of_the_game(self):
    # test 79
    """
    This test was drafted but never run.

    At this point in the development the decision was made to separate the printing of 
    scores into its own method, see `Bites.print_scores()`.
    `Bites.take_all_turns()` and `Bites.print_scores()` are then called in a third method; 
    `Bites.play_full_game()`.
    """
    pass
    # starting_trail = [
    #   "apple",
    #   None,
    #   None,
    #   "pepper",
    #   None,
    #   None,
    #   None,
    #   "bread",
    #   "pepper",
    #   None]
    # starting_ant_positions = {
    #   "purple": None,
    #   "brown": "anthill",
    #   "green": "anthill",
    #   "red": "anthill",
    #   "yellow": "anthill"}
    # starting_anthill = [None, "brown", "green", "red", "yellow"]

    # trail_after_turn_1_mario = starting_trail
    # ant_pos_after_turn_1_mario = {
    #   "purple": "anthill",
    #   "brown": "anthill",
    #   "green": "anthill",
    #   "red": "anthill",
    #   "yellow": "anthill"}
    # anthill_after_turn_1_mario = ["purple", "brown", "green", "red", "yellow"]

    # expected_new_trail = trail_after_turn_1_mario
    # expected_new_ant_positions = ant_pos_after_turn_1_mario
    # expected_new_anthill = anthill_after_turn_1_mario

    # ants = ["red", "yellow", "green", "brown", "purple"]
    # tokens_for_trail = {}
    
    # fake_mario = mock.MagicMock()
    # fake_mario.take_turn = mock.MagicMock(return_value = (
    #   trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario))
    # fake_mario.score_hand = mock.MagicMock(return_value = 3)
    # fake_luigi = mock.MagicMock()
    # fake_luigi.score_hand = mock.MagicMock(return_value = 9)

    # players = [fake_mario, fake_luigi]
    # bites_game = Bites(ants, tokens_for_trail, players)
    # bites_game.trail = starting_trail
    # bites_game.ant_positions = starting_ant_positions
    # bites_game.anthill = starting_anthill
    # bites_game.take_all_turns()

class PrintScoresTest(unittest.TestCase):
  def test_single_player_0_points_print_name_and_score(self):
    # test 80
    class FakePlayer():
      def __init__(self, name, score):
        self.name = name
        self.score = score

    ants = []
    tokens_for_trail = {}
    fake_mario = FakePlayer("mario", 0)
    players = [fake_mario]
    bites_game = Bites(ants, tokens_for_trail, players)

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_scores()
    print_mock.assert_called_once_with("mario: 0\n")
    self.assertEqual(print_mock.call_count, 1)
    print_patcher.stop()

  def test_two_players_prints_both_names_and_scores(self):
    # test 81
    class FakePlayer():
      def __init__(self, name, score):
        self.name = name
        self.score = score

    fake_mario = FakePlayer("mario", 3)
    fake_luigi = FakePlayer("luigi", 9)
    ants = []
    tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, tokens_for_trail, players)

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_scores()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("mario: 3\n"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("luigi: 9\n"))
    print_patcher.stop()

class PlayFullGameTest(unittest.TestCase):
  @patch('bites.Bites.take_all_turns')
  def test_play_full_game_calls_take_all_turns(self, take_all_turns_mock):
    # test 82
    bites_game = Bites([], {}, [])
    bites_game.play_full_game()
    self.assertTrue(take_all_turns_mock.called)

  @patch('bites.Bites.print_scores')
  def test_play_full_game_calls_print_scores(self, print_scores_mock):
    # test 83
    class FakePlayer():
      def __init__(self, name, score):
        self.name = name
        self.score = score
      
      def take_turn(self, trail, ant_positions, anthill):
        return (trail, ant_positions, anthill)

    fake_mario = FakePlayer("mario", 3)
    fake_luigi = FakePlayer("luigi", 9)
    players = [fake_mario, fake_luigi]
    bites_game = Bites([], {}, players)
    bites_game.play_full_game()
    self.assertTrue(print_scores_mock.called)

  @patch('bites.Bites.take_all_turns')
  @patch('bites.Bites.print_scores')
  def test_play_full_game_calls_take_all_turns_first_and_then_print_scores(
    # test 84
    self, print_scores_mock, take_all_turns_mock):
    manager = mock.Mock()
    manager.attach_mock(print_scores_mock, 'printing_the_score')
    manager.attach_mock(take_all_turns_mock, 'taking_all_the_turns')
    bites_game = Bites([], {}, [])
    bites_game.play_full_game()
    expected_calls = [
      mock.call.taking_all_the_turns(), 
      mock.call.printing_the_score()]
    self.assertEqual(manager.mock_calls, expected_calls)

class RenderGameTest(unittest.TestCase):
  def test_render_game_prints_player_name_and_hand_for_one_player(self):
    # test 85
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {}

    fake_mario = FakePlayer("mario")
    
    ants = []
    tokens_for_trail = {}
    players = [fake_mario]
    bites_game = Bites(ants, tokens_for_trail, players)

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 1)
    self.assertEqual(print_mock.call_args_list[0], mock.call("mario: {}"))
    print_patcher.stop()

  def test_render_game_prints_player_names_and_hands_for_two_players(self):
    # test 86
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {}

    fake_mario = FakePlayer("mario")
    fake_luigi = FakePlayer("luigi")

    ants = []
    tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, tokens_for_trail, players)

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("mario: {}"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("luigi: {}"))
    print_patcher.stop()

  def test_render_game_prints_food_token_for_trail_of_len_1(self):
    # test 87
    ants = []
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = ["pepper"]

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 1)
    self.assertEqual(print_mock.call_args_list[0], mock.call("pepper"))
    print_patcher.stop()

  def test_render_game_prints_food_tokens_for_trail_len_greater_than_1(self):
    # test 88
    ants = []
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = ["pepper", "apple", "grapes", "cheese", "bread"]

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 5)
    self.assertEqual(print_mock.call_args_list[0], mock.call("pepper"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("apple"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("grapes"))
    self.assertEqual(print_mock.call_args_list[3], mock.call("cheese"))
    self.assertEqual(print_mock.call_args_list[4], mock.call("bread"))
    print_patcher.stop()

  def test_check_render_game_prints_players_and_trail(self):
    # test 89
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {}

    fake_mario = FakePlayer("mario")
    fake_luigi = FakePlayer("luigi")

    ants = []
    tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = ["pepper", "apple", "grapes", "cheese", "bread"]

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 7)
    self.assertEqual(print_mock.call_args_list[0], mock.call("mario: {}"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("luigi: {}"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("pepper"))
    self.assertEqual(print_mock.call_args_list[3], mock.call("apple"))
    self.assertEqual(print_mock.call_args_list[4], mock.call("grapes"))
    self.assertEqual(print_mock.call_args_list[5], mock.call("cheese"))
    self.assertEqual(print_mock.call_args_list[6], mock.call("bread"))
    print_patcher.stop()

  def test_render_game_prints_ants_positioned_before_the_trail(self):
    # test 90
    ants = []
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.ant_positions = {"red": None}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 1)
    self.assertEqual(print_mock.call_args_list[0], mock.call("red"))
    print_patcher.stop()

  def test_render_game_shows_ants_positioned_on_trail_in_correct_place(self):
    # test 91
    ants = []
    tokens_for_trail = {"apple" :1}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.ant_positions = {"red": 0}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 1)
    self.assertEqual(print_mock.call_args_list[0], mock.call("apple red"))
    print_patcher.stop()

  def test_check_render_game_shows_player_names_and_hands__ants_waiting_to_start__and_trail_with_ants(
    self):
    # test 92
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {}

    fake_mario = FakePlayer("mario")
    fake_luigi = FakePlayer("luigi")

    ants = []
    tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = ["pepper", "apple", "grapes", "cheese", "bread"]
    bites_game.ant_positions = {"green": 0, "purple": 2, "brown": 4, "red": None, "yellow": None}
    
    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 9)
    self.assertEqual(print_mock.call_args_list[0], mock.call("mario: {}"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("luigi: {}"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("red"))
    self.assertEqual(print_mock.call_args_list[3], mock.call("yellow"))
    self.assertEqual(print_mock.call_args_list[4], mock.call("pepper green"))
    self.assertEqual(print_mock.call_args_list[5], mock.call("apple"))
    self.assertEqual(print_mock.call_args_list[6], mock.call("grapes purple"))
    self.assertEqual(print_mock.call_args_list[7], mock.call("cheese"))
    self.assertEqual(print_mock.call_args_list[8], mock.call("bread brown"))
    print_patcher.stop()

  def test_render_game_shows_ant_positioned_on_anthill(self):
    # test 93
    ants = []
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = ["yellow"]

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    self.assertEqual(print_mock.call_count, 1)
    self.assertEqual(print_mock.call_args_list[0], mock.call("yellow"))
    print_patcher.stop()

  def test_render_game_shows_two_ants_positioned_on_anthill_higher_one_first(self):
    # test 94
    ants = []
    tokens_for_trail = {}
    players = []
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill", "green": "anthill"}
    bites_game.anthill = ["yellow", "green"]

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.render_game()
    # self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("green"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("yellow"))
    print_patcher.stop()




if __name__ == '__main__':
  unittest.main(verbosity = 2)
