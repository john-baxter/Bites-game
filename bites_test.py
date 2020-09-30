import unittest
from unittest import mock
from bites import Bites
from player import Player

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
  # test 1
  def test_can_initialise_one_ant(self):
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
      "brown": None,
      }
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

class InitialiseTrailTest(unittest.TestCase):
  # test 4
  def test_can_initialise_trail_with_one_token(self):
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
      ["apple", "apple", "grapes"]
      ]
    self.assertIn(bites_game.trail, expected_trails)

  def test_full_size_trail_using_count_method_and_length(self):
  # test 8
    foods = {
      "apple": 9,
      "grapes": 9,
      "cheese": 9,
      "pepper": 9,
      "bread": 9
    }
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

class PlayTest(unittest.TestCase):
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

    bites_game.play()

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
    
    bites_game.play()
    
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
    bites_game.play()
    
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
    bites_game.play()

    self.assertEqual(fake_mario.take_turn.call_count, 1)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill))
    self.assertEqual(bites_game.trail, expected_new_trail)
    self.assertEqual(bites_game.ant_positions, expected_new_ant_positions)
    self.assertEqual(bites_game.anthill, expected_new_anthill)

  def test_final_scores_are_printed_at_the_end_of_the_game(self):
  # test 79
    """
    Starting point is the game situation from the previous game at the point of the penultimate 
    turn has been completed. The same final move will be executed here and the scores analysed.
    P0 plays purple ant, picks food from XX
    """
    pass
    # players = [FakePlayer(), FakePlayer()]
    # ants = ["red", "yellow", "green", "brown", "purple"]
    # tokens_for_trail = {}
    # bites_game = Bites(ants, tokens_for_trail, players)
    # bites_game.trail = [
    #   "apple", 
    #   "cheese", 
    #   None, 
    #   None, 
    #   None, 
    #   "apple", 
    #   None, 
    #   "bread", 
    #   "pepper", 
    #   "grapes"]
    # bites_game.ant_positions = {
    #   "red": "anthill",
    #   "yellow": "anthill",
    #   "green": "anthill",
    #   "brown": "anthill",
    #   "purple": None}

    # bites_game.play()

    # expected_new_trail = [
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
    # expected_new_ant_positions = {
    #   "red": "anthill",
    #   "yellow": "anthill",
    #   "green": "anthill",
    #   "brown": "anthill",
    #   "purple": "anthill"}
    # expected_new_anthill = ["purple", "brown", "green", "red", "yellow"]
    # expected_P0_points = 4 
    # expected_P1_points = 8
    # self.assertEqual(bites_game.players[0].score, expected_P0_points )
    # self.assertEqual(bites_game.players[1].score, expected_P1_points )

if __name__ == '__main__':
  unittest.main(verbosity = 2)
