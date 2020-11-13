import unittest
from unittest import mock
from unittest.mock import patch, call
from bites import Bites

class BitesInitTest(unittest.TestCase):
  def test___init___method_works(self):
    # test 36
    # This test was written rertrospectively; the __init__ method came about 
    # naturally during refactoring of the code into the Bites class.
    test_ants = ['purple', 'yellow']
    test_standard_tokens = {
      'grapes': 1,
      'cheese': 1}
    test_special_tokens = {}
    test_players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    bites_game = Bites(test_ants, test_standard_tokens, test_special_tokens, test_players, anthill_rule, wine_rule)
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
    self.assertEqual(bites_game.standard_tokens_for_trail, test_standard_tokens)

  def test_bites_class_can_receive_instance_of_player_class(self):
    # test 73
    class FakePlayer():
      pass

    mario = FakePlayer()
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, [mario], anthill_rule, wine_rule)
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
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    self.assertEqual(len(bites_game.players), 2)
    self.assertEqual(bites_game.players[0].name, "mario")
    self.assertEqual(bites_game.players[1].name, "luigi")

  def test_anthill_food_tokens_are_initialised_when_Bites_class_is_instantiated(self):
    # test 118
    ants = []
    standard_tokens_for_trail = {
      "apple": 0,
      "grapes": 0,
      "bread": 0,
      "cheese": 0,
      "pepper": 0}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_anthill_food = {
      "apple": 1,
      "grapes": 1,
      "bread": 1,
      "cheese": 1,
      "pepper": 1}
    actual_anthill_food = bites_game.anthill_food_tokens
    self.assertEqual(actual_anthill_food, expected_anthill_food)

  def test_Bites_receives_anthill_rule_as_string_and_stores_it_as_attribute(self):
    # test 142
    ants = []
    standard_tokens_for_trail = {"apple": 0}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)

    expected_anthill_rule_attribute_type = str
    expected_anthill_rule_attribute = anthill_rule

    self.assertEqual(type(bites_game.anthill_rule), expected_anthill_rule_attribute_type)
    self.assertEqual(bites_game.anthill_rule, expected_anthill_rule_attribute)

  def test_Bites_receives_wine_rule_as_string_and_stores_it_as_attribute(self):
    # test 175
    ants = []
    standard_tokens_for_trail = {"apple": 0}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    
    expected_wine_rule_attribute_type = str
    expected_wine_rule_attribute = "test wine rule"

    self.assertEqual(type(bites_game.wine_rule), expected_wine_rule_attribute_type)
    self.assertEqual(bites_game.wine_rule, expected_wine_rule_attribute)

class InitialiseAntsTest(unittest.TestCase):
  def test_can_initialise_one_ant(self):
    # test 1
    ants = ["red"]
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_ant_positions = {"red": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_two_ants(self):
    # test 2
    ants = ["red", "purple"]
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_ant_positions = {"red": None, "purple": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_five_ants(self):
    # test 3
    ants = ["red", "purple", "yellow", "green", "brown"]
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
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
    standard_tokens_for_trail = {"apple": 1}
    special_tokens_for_trail = {}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_trail = ["apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_initialise_trail_with_two_different_tokens(self):
    # test 5
    standard_tokens_for_trail = {"apple": 1, "grapes": 1}
    special_tokens_for_trail = {}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_trails = [["apple", "grapes"], ["grapes", "apple"]]
    self.assertIn(bites_game.trail, expected_trails)

  def test_can_initialise_trail_with_five_of_same_token(self):
    # test 6
    standard_tokens_for_trail = {"apple": 5}
    special_tokens_for_trail = {}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_trail = ["apple", "apple", "apple", "apple", "apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_shuffle_two_plus_one_tokens(self):
    # test 7
    standard_tokens_for_trail = {"apple": 2, "grapes": 1}
    special_tokens_for_trail = {}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_trails = [
      ["grapes", "apple", "apple"],
      ["apple", "grapes", "apple"],
      ["apple", "apple", "grapes"]]
    self.assertIn(bites_game.trail, expected_trails)

  def test_full_size_trail_using_count_method_and_length(self):
    # test 8
    standard_tokens_for_trail = {
      "apple": 9,
      "grapes": 9,
      "cheese": 9,
      "pepper": 9,
      "bread": 9}
    special_tokens_for_trail = {}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_trail_length = 45
    self.assertEqual(len(bites_game.trail), expected_trail_length)
    self.assertEqual(bites_game.trail.count("apple"), 9)
    self.assertEqual(bites_game.trail.count("grapes"), 9)
    self.assertEqual(bites_game.trail.count("cheese"), 9)
    self.assertEqual(bites_game.trail.count("pepper"), 9)
    self.assertEqual(bites_game.trail.count("bread"), 9)

  def test_full_size_trail_inc_five_wines(self):
    # test 154
    standard_tokens_for_trail = {
      "apple": 9,
      "grapes": 9,
      "cheese": 9,
      "pepper": 9,
      "bread": 9}
    special_tokens_for_trail = {"wine": 5}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_trail_length = 50
    self.assertEqual(len(bites_game.trail), expected_trail_length)
    self.assertEqual(bites_game.trail.count("apple"), 9)
    self.assertEqual(bites_game.trail.count("grapes"), 9)
    self.assertEqual(bites_game.trail.count("cheese"), 9)
    self.assertEqual(bites_game.trail.count("pepper"), 9)
    self.assertEqual(bites_game.trail.count("bread"), 9)
    self.assertEqual(bites_game.trail.count("wine"), 5)

  def test_check_full_size_trail_inc_five_chocolate(self):
    # test 184
    standard_tokens_for_trail = {
      "apple": 9,
      "grapes": 9,
      "cheese": 9,
      "pepper": 9,
      "bread": 9}
    special_tokens_for_trail = {
      "wine": 5,
      "chocolate": 5,
      }
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_trail_length = 55
    self.assertEqual(len(bites_game.trail), expected_trail_length)
    self.assertEqual(bites_game.trail.count("apple"), 9)
    self.assertEqual(bites_game.trail.count("grapes"), 9)
    self.assertEqual(bites_game.trail.count("cheese"), 9)
    self.assertEqual(bites_game.trail.count("pepper"), 9)
    self.assertEqual(bites_game.trail.count("bread"), 9)
    self.assertEqual(bites_game.trail.count("wine"), 5)
    self.assertEqual(bites_game.trail.count("chocolate"), 5)

class InitialiseAnthillTest(unittest.TestCase):
  def test_can_initialise_anthill_as_list_with_len_five_and_every_element_is_None(self):
    # test 27
    ants = ['purple', 'red', 'brown', 'yellow', 'green']
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    expected_anthill = [None, None, None, None, None]
    self.assertEqual(bites_game.anthill, expected_anthill)

class TakeAllTurnsTest(unittest.TestCase):
  @patch('bites.Bites.render_game')
  def test_first_player_takes_one_turn(self, render_game_mock):
    # test 75
    starting_trail = ["apple", "apple"]
    starting_ant_positions = {
      "red": None,
      "yellow": None,
      "green": None,
      "brown": None,
      "purple": None}
    starting_anthill = [None, None, None, None, None]
    starting_anthill_food_tokens = {}
    
    trail_after_turn_1_mario = ["apple", None]
    ant_pos_after_turn_1_mario = {
      "red": 0,
      "yellow": None,
      "green": None,
      "brown": None,
      "purple": None}
    anthill_after_turn_1_mario = starting_anthill
    anthill_food_tokens_after_turn_1_mario = starting_anthill_food_tokens

    expected_new_trail = trail_after_turn_1_mario
    expected_new_ant_positions = ant_pos_after_turn_1_mario
    expected_new_anthill = starting_anthill
    expected_new_anthill_food_tokens = starting_anthill_food_tokens
    
    fake_mario = mock.MagicMock()
    players = [fake_mario]
    ants = ["red", "yellow", "green", "brown", "purple"]
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    anthill_rule = ""
    wine_rule = ""
    
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill
    bites_game.anthill_food_tokens = starting_anthill_food_tokens
    bites_game.anthill_rule = "top down"
    
    fake_mario.take_turn = mock.MagicMock(side_effect = [(
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, anthill_food_tokens_after_turn_1_mario),
      ([], {}, [], {})])
    
    bites_game.take_all_turns()

    self.assertGreaterEqual(fake_mario.take_turn.call_count, 1)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill, bites_game.anthill_rule, starting_anthill_food_tokens))
    self.assertGreaterEqual(render_game_mock.call_count, 2)
  
  @patch('bites.Bites.render_game')
  def test_one_whole_round_is_played(self, render_game_mock):
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
    starting_anthill_food_tokens = {}
    
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
    anthill_food_tokens_after_turn_1_mario = starting_anthill_food_tokens
    
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
    anthill_food_tokens_after_turn_2_luigi = starting_anthill_food_tokens
    
    expected_new_trail = trail_after_turn_2_luigi
    expected_new_ant_positions = ant_pos_after_turn_2_luigi
    expected_new_anthill = starting_anthill
    expected_new_anthill_food_tokens = starting_anthill_food_tokens
    
    fake_mario = mock.MagicMock()
    fake_luigi = mock.MagicMock()
    players = [fake_mario, fake_luigi]
    ants = ["red", "yellow", "green", "brown", "purple"]
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    
    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill
    bites_game.anthill_rule = "top down"
    
    fake_mario.take_turn = mock.MagicMock(side_effect = [
      (trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, anthill_food_tokens_after_turn_1_mario),
      ([], {}, [], {})])
    
    fake_luigi.take_turn = mock.MagicMock(return_value = (
      trail_after_turn_2_luigi, ant_pos_after_turn_2_luigi, anthill_after_turn_2_luigi, anthill_food_tokens_after_turn_2_luigi))
    
    bites_game.take_all_turns()
    
    self.assertGreaterEqual(fake_mario.take_turn.call_count, 1)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill, bites_game.anthill_rule, starting_anthill_food_tokens))
    self.assertGreaterEqual(fake_luigi.take_turn.call_count, 1)
    self.assertEqual(fake_luigi.take_turn.call_args_list[0], mock.call(
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, bites_game.anthill_rule, anthill_food_tokens_after_turn_1_mario))
    self.assertGreaterEqual(render_game_mock.call_count, 3)

  @patch('bites.Bites.render_game')
  def test_two_full_rounds_are_played(self, render_game_mock):
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
    starting_anthill_food_tokens = {}

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
    anthill_food_tokens_after_turn_1_mario = starting_anthill_food_tokens
    
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
    anthill_food_tokens_after_turn_2_luigi = starting_anthill_food_tokens

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
    anthill_food_tokens_after_turn_3_mario = starting_anthill_food_tokens
    
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
    anthill_food_tokens_after_turn_4_luigi = starting_anthill_food_tokens

    expected_new_trail = trail_after_turn_4_luigi 
    expected_new_ant_positions = ant_pos_after_turn_4_luigi
    expected_new_anthill = anthill_after_turn_4_luigi

    ants = ["red", "yellow", "green", "brown", "purple"]
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    anthill_rule = ""
    wine_rule = ""
    fake_mario = mock.MagicMock()
    fake_luigi = mock.MagicMock()
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill
    bites_game.anthill_food_tokens = starting_anthill_food_tokens
    bites_game.anthill_rule = "top down"
    
    fake_mario.take_turn = mock.MagicMock(side_effect = [
      (trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, anthill_food_tokens_after_turn_1_mario),
      (trail_after_turn_3_mario, ant_pos_after_turn_3_mario, anthill_after_turn_3_mario, anthill_food_tokens_after_turn_3_mario),
      ([], {}, [], {})])

    fake_luigi.take_turn = mock.MagicMock(side_effect = [
      (trail_after_turn_2_luigi, ant_pos_after_turn_2_luigi, anthill_after_turn_2_luigi, anthill_food_tokens_after_turn_2_luigi),
      (trail_after_turn_4_luigi, ant_pos_after_turn_4_luigi, anthill_after_turn_4_luigi, anthill_food_tokens_after_turn_4_luigi)])
    
    bites_game.take_all_turns()
    
    self.assertGreaterEqual(fake_mario.take_turn.call_count, 2)
    self.assertEqual(fake_luigi.take_turn.call_count, 2)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill, bites_game.anthill_rule, starting_anthill_food_tokens))
    self.assertEqual(fake_luigi.take_turn.call_args_list[0], mock.call(
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, bites_game.anthill_rule, anthill_food_tokens_after_turn_1_mario))
    self.assertEqual(fake_mario.take_turn.call_args_list[1], mock.call(
      trail_after_turn_2_luigi, ant_pos_after_turn_2_luigi, anthill_after_turn_2_luigi, bites_game.anthill_rule, anthill_food_tokens_after_turn_2_luigi))
    self.assertEqual(fake_luigi.take_turn.call_args_list[1], mock.call(
      trail_after_turn_3_mario, ant_pos_after_turn_3_mario, anthill_after_turn_3_mario, bites_game.anthill_rule, anthill_food_tokens_after_turn_3_mario))
    self.assertGreaterEqual(render_game_mock.call_count, 5)

  @patch('bites.Bites.render_game')
  def test_the_game_is_played_until_all_ants_are_on_the_anthill(self, render_game_mock):
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
    starting_anthill_food_tokens = {"grapes": 1}

    trail_after_turn_1_mario = starting_trail
    ant_pos_after_turn_1_mario = {
      "purple": "anthill",
      "brown": "anthill",
      "green": "anthill",
      "red": "anthill",
      "yellow": "anthill"}
    anthill_after_turn_1_mario = ["purple", "brown", "green", "red", "yellow"]
    anthill_food_tokens_after_turn_1_mario = {"grapes": 0}

    expected_new_trail = trail_after_turn_1_mario
    expected_new_ant_positions = ant_pos_after_turn_1_mario
    expected_new_anthill = anthill_after_turn_1_mario
    expected_new_anthill_food_tokens = anthill_food_tokens_after_turn_1_mario

    fake_mario = mock.MagicMock()
    players = [fake_mario]
    ants = ["red", "yellow", "green", "brown", "purple"]
    standard_tokens_for_trail = {"grapes": 0}
    special_tokens_for_trail = {}
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = starting_trail
    bites_game.ant_positions = starting_ant_positions
    bites_game.anthill = starting_anthill
    bites_game.anthill_rule = "top down"
    
    fake_mario.take_turn = mock.MagicMock(return_value = (
      trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, anthill_food_tokens_after_turn_1_mario))

    bites_game.take_all_turns()

    self.assertEqual(fake_mario.take_turn.call_count, 1)
    self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
      starting_trail, starting_ant_positions, starting_anthill, bites_game.anthill_rule, starting_anthill_food_tokens))
    self.assertEqual(bites_game.trail, expected_new_trail)
    self.assertEqual(bites_game.ant_positions, expected_new_ant_positions)
    self.assertEqual(bites_game.anthill, expected_new_anthill)
    self.assertEqual(bites_game.anthill_food_tokens, expected_new_anthill_food_tokens)
    self.assertEqual(render_game_mock.call_count, 2)

  def test_final_scores_are_printed_at_the_end_of_the_game(self):
    # test 79
    """
    This test was drafted but never run.

    At this point in the development the decision was made to separate the printing of 
    scores into its own method, see `Bites.calculate_and_print_scores()`.
    `Bites.take_all_turns()` and `Bites.calculate_and_print_scores()` are then called in a third method; 
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
    # fake_mario.score_food = mock.MagicMock(return_value = 3)
    # fake_luigi = mock.MagicMock()
    # fake_luigi.score_food = mock.MagicMock(return_value = 9)

    # players = [fake_mario, fake_luigi]
    # bites_game = Bites(ants, tokens_for_trail, players, anthill_rule)
    # bites_game.trail = starting_trail
    # bites_game.ant_positions = starting_ant_positions
    # bites_game.anthill = starting_anthill
    # bites_game.take_all_turns()

class PrintScoresTest(unittest.TestCase):
  def test_single_player_0_points_print_name_and_score(self):
    # test 80
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.score = 0

      def score_hand(self, anthill, standard_tokens_for_trail):
        pass

    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    fake_mario = FakePlayer("mario")
    players = [fake_mario]
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.calculate_and_print_scores()
    self.assertEqual(print_mock.call_args_list[1], mock.call("mario: 0"))
    self.assertGreaterEqual(print_mock.call_count, 1)
    print_patcher.stop()

  def test_two_players_prints_both_names_and_scores(self):
    # test 81
    class FakePlayer():
      def __init__(self, name, final_score):
        self.name = name
        self.score = 0
        self.final_score = final_score

      def score_hand(self, anthill, standard_tokens_for_trail):
        self.score = self.final_score

    fake_mario = FakePlayer("mario", 3)
    fake_luigi = FakePlayer("luigi", 9)
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.calculate_and_print_scores()
    self.assertGreaterEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[1], mock.call("mario: 3"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("luigi: 9"))
    print_patcher.stop()

class PlayFullGameTest(unittest.TestCase):
  @patch('bites.Bites.take_all_turns')
  @patch('bites.Bites.calculate_and_print_scores')
  def test_play_full_game_calls_take_all_turns(self, calculate_and_print_scores_mock, take_all_turns_mock):
    # test 82
    bites_game = Bites([], {}, {}, [], "", "")
    bites_game.play_full_game()
    self.assertTrue(take_all_turns_mock.called)

  @patch('bites.Bites.take_all_turns')
  @patch('bites.Bites.calculate_and_print_scores')
  def test_play_full_game_calls_calculate_and_print_scores(self, calculate_and_print_scores_mock, take_all_turns_mock):
    # test 83
    class FakePlayer():
      def __init__(self, name, score):
        self.name = name
        self.score = score
        self.hand = {}
      
      def take_turn(self, trail, ant_positions, anthill):
        return (trail, ant_positions, anthill)

    fake_mario = FakePlayer("mario", 3)
    fake_luigi = FakePlayer("luigi", 9)
    players = [fake_mario, fake_luigi]
    bites_game = Bites([], {}, {}, [], players, "")
    bites_game.play_full_game()
    calculate_and_print_scores_mock.assert_called_once_with()

  @patch('bites.Bites.take_all_turns')
  @patch('bites.Bites.calculate_and_print_scores')
  def test_play_full_game_calls_take_all_turns_first_and_then_calculate_and_print_scores(
    self, calculate_and_print_scores_mock, take_all_turns_mock):
    # test 84
    manager = mock.Mock()
    manager.attach_mock(calculate_and_print_scores_mock, 'printing_the_score')
    manager.attach_mock(take_all_turns_mock, 'taking_all_the_turns')
    bites_game = Bites([], {}, {}, [], "", "")
    bites_game.play_full_game()
    expected_calls = [
      mock.call.taking_all_the_turns(), 
      mock.call.printing_the_score()]
    self.assertEqual(manager.mock_calls, expected_calls)

class RenderGameTest(unittest.TestCase):
  @patch('bites.Bites.print_wine_rule_statement')
  @patch('bites.Bites.print_players_names_and_hands')
  @patch('bites.Bites.print_ants_positioned_before_the_trail')
  @patch('bites.Bites.print_trail_and_ants_positioned_thereon')
  @patch('bites.Bites.print_ants_positioned_on_anthill_top_down')
  @patch('bites.Bites.print_anthill_food_tokens')
  def test_render_game_calls_all_appropriate_sub_methods_in_correct_order(
    self,
    mock_anthill_food_print,
    mock_anthill_placement_print,
    mock_trail_and_ants_print,
    mock_ants_pre_trail_print,
    mock_player_details_print,
    mock_wine_rule_print,
    ):
    # test 183
    manager = mock.Mock()
    manager.attach_mock(mock_wine_rule_print, 'mock_wine_rule_print')
    manager.attach_mock(mock_player_details_print, 'mock_player_details_print')
    manager.attach_mock(mock_ants_pre_trail_print, 'mock_ants_pre_trail_print')
    manager.attach_mock(mock_trail_and_ants_print, 'mock_trail_and_ants_print')
    manager.attach_mock(mock_anthill_placement_print, 'mock_anthill_placement_print')
    manager.attach_mock(mock_anthill_food_print, 'mock_anthill_food_print')
    
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = "oenophile"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.ant_positions = {"random key": None}

    bites_game.render_game()

    expected_mock_calls = [
    mock.call.mock_wine_rule_print(),
    mock.call.mock_player_details_print(),
    mock.call.mock_ants_pre_trail_print(),
    mock.call.mock_trail_and_ants_print(),
    mock.call.mock_anthill_placement_print(),
    mock.call.mock_anthill_food_print(),
    ]

    self.assertEqual(manager.mock_calls, expected_mock_calls)
    mock_anthill_food_print.assert_called_once()
    mock_anthill_placement_print.assert_called_once()
    mock_trail_and_ants_print.assert_called_once()
    mock_ants_pre_trail_print.assert_called_once()
    mock_player_details_print.assert_called_once()
    mock_wine_rule_print.assert_called_once()

  def test_print_players_names_and_hands_prints_player_name_and_hand_for_one_player(self):
    # test 85
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {}

    fake_mario = FakePlayer("mario")
    
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = [fake_mario]
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.ant_positions = {"random key": None}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_players_names_and_hands()
    self.assertGreaterEqual(print_mock.call_count, 1)
    self.assertEqual(print_mock.call_args_list[1], mock.call("mario: {}"))
    print_patcher.stop()

  def test_print_players_names_and_hands_prints_name_and_non_empty_hand_for_one_player(self):
    # test 96
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {"bread": 2, "cheese": 1}

    fake_mario = FakePlayer("mario")
    
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = [fake_mario]
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.ant_positions = {"random key": None}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_players_names_and_hands()
    self.assertGreaterEqual(print_mock.call_count, 1)
    self.assertEqual(print_mock.call_args_list[1], mock.call("mario: {'bread': 2, 'cheese': 1}"))
    print_patcher.stop()

  def test_print_players_names_and_hands_prints_player_names_and_hands_for_two_players(self):
    # test 86
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {}

    fake_mario = FakePlayer("mario")
    fake_luigi = FakePlayer("luigi")

    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.ant_positions = {"random key": None}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_players_names_and_hands()
    self.assertGreaterEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[1], mock.call("mario: {}"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("luigi: {}"))
    print_patcher.stop()

  def test_print_trail_and_ants_prints_food_token_for_trail_of_len_1(self):
    # test 87
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = ["pepper"]
    bites_game.ant_positions = {"random key": None}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_trail_and_ants_positioned_thereon()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nTrail:"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("pepper"))
    print_patcher.stop()

  def test_print_trail_and_ants_prints_food_tokens_for_trail_len_greater_than_1(self):
    # test 88
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = ["pepper", "apple", "grapes", "cheese", "bread"]
    bites_game.ant_positions = {"random key": None}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_trail_and_ants_positioned_thereon()
    self.assertEqual(print_mock.call_count, 6)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nTrail:"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("pepper"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("apple"))
    self.assertEqual(print_mock.call_args_list[3], mock.call("grapes"))
    self.assertEqual(print_mock.call_args_list[4], mock.call("cheese"))
    self.assertEqual(print_mock.call_args_list[5], mock.call("bread"))
    print_patcher.stop()

  def test_print_ants_before_trail_prints_ants_positioned_before_the_trail(self):
    # test 90
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.ant_positions = {"red": None}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_ants_positioned_before_the_trail()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nAnts at the beginning of the trail:"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("red"))
    print_patcher.stop()

  def test_print_trail_and_ants_shows_ants_positioned_on_trail_in_correct_place(self):
    # test 91
    ants = []
    standard_tokens_for_trail = {"apple" :1}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.ant_positions = {"red": 0}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_trail_and_ants_positioned_thereon()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nTrail and ant positions:"))
    self.assertEqual(print_mock.call_args_list[1], mock.call("apple red"))
    print_patcher.stop()

  def test_print_ants_on_anthill_shows_ant_positioned_on_anthill(self):
    # test 93
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = ["yellow"]

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_ants_positioned_on_anthill_top_down()
    self.assertEqual(print_mock.call_count, 3)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nAnthill:"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("The yellow ant is in level 0"))
    print_patcher.stop()

  def test_print_ants_on_anthill_shows_two_ants_positioned_on_anthill_higher_one_first(self):
    # test 94
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill", "green": "anthill"}
    bites_game.anthill = ["yellow", "green"]

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_ants_positioned_on_anthill_top_down()
    self.assertEqual(print_mock.call_count, 4)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nAnthill:"))
    self.assertEqual(print_mock.call_args_list[2], mock.call("The green ant is in level 1"))
    self.assertEqual(print_mock.call_args_list[3], mock.call("The yellow ant is in level 0"))
    print_patcher.stop()

  def test_print_anthill_food_shows_anthill_food_for_single_food_token(self):
    # test 127
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = []
    bites_game.anthill_food_tokens = {"grapes": 1}
    
    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_anthill_food_tokens()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nAnthill food tokens"))
    self.assertEqual(print_mock.call_args_list[1], mock.call(["grapes"]))
    print_patcher.stop()

  def test_print_anthill_food_shows_anthill_food_for_one_each_of_two_foods(self):
    # test 128
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = []
    bites_game.anthill_food_tokens = {"grapes": 1, "pepper": 1}
    
    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_anthill_food_tokens()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nAnthill food tokens"))
    self.assertEqual(print_mock.call_args_list[1], mock.call(["grapes", "pepper"]))
    print_patcher.stop()

  def test_print_anthill_food_shows_anthill_food_for_two_of_the_same_food(self):
    # test 129
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = []
    bites_game.anthill_food_tokens = {"grapes": 2}
    
    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_anthill_food_tokens()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nAnthill food tokens"))
    self.assertEqual(print_mock.call_args_list[1], mock.call(["grapes", "grapes"]))
    print_patcher.stop()

  def test_check_print_anthill_food_does_not_show_food_type_if_v_equals_0(self):
    # test 130
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = []
    bites_game.anthill_food_tokens = {"grapes": 1, "pepper": 1, "bread": 0}
    
    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_anthill_food_tokens()
    self.assertEqual(print_mock.call_count, 2)
    self.assertEqual(print_mock.call_args_list[0], mock.call("\nAnthill food tokens"))
    self.assertEqual(print_mock.call_args_list[1], mock.call(["grapes", "pepper"]))
    print_patcher.stop()

  def test_print_trail_replaces_trail_element_None_with_placeholder(self):
    # test 131
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = [
      "apple",
      None,
      None,
      "bread",
      "grapes",
      "cheese",
      None]
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = []
    bites_game.anthill_food_tokens = {}

    print_patcher = mock.patch('builtins.print')
    print_mock = print_patcher.start()
    bites_game.print_trail_and_ants_positioned_thereon()
    self.assertEqual(print_mock.call_count, 8)
    self.assertEqual(print_mock.call_args_list[2], mock.call("--"))
    self.assertEqual(print_mock.call_args_list[3], mock.call("--"))
    self.assertEqual(print_mock.call_args_list[7], mock.call("--"))
    print_patcher.stop()

  @patch('builtins.print')
  def test_print_ants_on_anthill_shows_anthill_rule_next_to_anthill(self, mock_builtin_print):
    # test 145
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.trail = []
    bites_game.ant_positions = {"yellow": "anthill"}
    bites_game.anthill = ["yellow"]

    bites_game.print_ants_positioned_on_anthill_top_down()

    expected_print_result_0 = call("\nAnthill:")
    expected_print_result_1 = call("Ants will be placed on the anthill according to the rule: test anthill order")
    expected_print_result_2 = call("The yellow ant is in level 0")

    self.assertEqual(mock_builtin_print.call_args_list[0], expected_print_result_0)
    self.assertEqual(mock_builtin_print.call_args_list[1], expected_print_result_1)
    self.assertEqual(mock_builtin_print.call_args_list[2], expected_print_result_2)

  @patch('builtins.print')
  def test_render_game_prints_statement_about_wine_rule(self, mock_builtin_print):
    # test 182
    ants = []
    standard_tokens_for_trail = {}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = "oenophile"
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    bites_game.ant_positions = {"random key": None}

    bites_game.print_wine_rule_statement()

    expected_print_result_0 = call("\nThe wine scoring card currently in play is: ")
    expected_print_result_1 = call("Oenophile")

    self.assertEqual(mock_builtin_print.call_args_list[0], expected_print_result_0)
    self.assertEqual(mock_builtin_print.call_args_list[1], expected_print_result_1)

class InitialiseAnthillFoodTokensTest(unittest.TestCase):
  def test_anthill_can_store_food_tokens_in_dict(self):
    # test 116
    ants = []
    standard_tokens_for_trail = {
      "apple": 0,
      "grapes": 0,
      "bread": 0,
      "cheese": 0,
      "pepper": 0}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    self.assertIsInstance(bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail), dict)

  def test_upon_initialisation_anthill_has_one_of_each_type_of_food(self):
    # test 117
    ants = []
    standard_tokens_for_trail = {
      "apple": 0,
      "grapes": 0,
      "bread": 0,
      "cheese": 0,
      "pepper": 0}
    special_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail)), 5)
    self.assertEqual(list(bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail).values()), [1, 1, 1, 1, 1])
    self.assertIn("apple", bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail).keys())
    self.assertIn("grapes", bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail).keys())
    self.assertIn("bread", bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail).keys())
    self.assertIn("cheese", bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail).keys())
    self.assertIn("pepper", bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail).keys())
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens(standard_tokens_for_trail).keys()), 5)

  def test_upon_initialisation_anthill_does_not_have_wine(self):
    # test 167
    ants = []
    standard_tokens = {
      "apple": 0,
      "grapes": 0,
      "bread": 0,
      "cheese": 0,
      "pepper": 0}
    special_tokens = {"wine": 0}
    players = []
    anthill_rule = ""
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens, special_tokens, players, anthill_rule, wine_rule)
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens(standard_tokens)), 5)
    self.assertEqual(list(bites_game.initialise_anthill_food_tokens(standard_tokens).values()), [1, 1, 1, 1, 1])
    self.assertIn("apple", bites_game.initialise_anthill_food_tokens(standard_tokens).keys())
    self.assertIn("grapes", bites_game.initialise_anthill_food_tokens(standard_tokens).keys())
    self.assertIn("bread", bites_game.initialise_anthill_food_tokens(standard_tokens).keys())
    self.assertIn("cheese", bites_game.initialise_anthill_food_tokens(standard_tokens).keys())
    self.assertIn("pepper", bites_game.initialise_anthill_food_tokens(standard_tokens).keys())
    self.assertNotIn("wine", bites_game.initialise_anthill_food_tokens(standard_tokens).keys())
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens(standard_tokens).keys()), 5)

class VerifyChocolatePositionsTest(unittest.TestCase):
  def test_verify_chocolate_positions_returns_a_list(self):
    # test 185
    ants = []
    standard_tokens_for_trail = {} 
    special_tokens_for_trail = {}
    players = []
    anthill_rule = "" 
    wine_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, special_tokens_for_trail, players, anthill_rule, wine_rule)
    
    expected_result = list
    actual_result = bites_game.verify_chocolate_positions()
    self.assertIsInstance(actual_result, expected_result)

if __name__ == '__main__':
  unittest.main(verbosity = 2)
