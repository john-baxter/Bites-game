import unittest
from unittest import mock
from unittest.mock import patch, call
from bites import Bites

class BitesInitTest(unittest.TestCase):
  def test___init___method_works(self):
    # test 36
    # This test was written retrospectively; the __init__ method came about 
    # naturally during refactoring of the code into the Bites class.
    test_ants = ['purple', 'yellow']
    test_standard_tokens = {
      'grapes': 1,
      'cheese': 1}
    test_wine_tokens = {}
    chocolate_tokens_for_trail = {"chocolate": 0}
    test_players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(test_ants, test_standard_tokens, test_wine_tokens, chocolate_tokens_for_trail, test_players, anthill_rule, wine_rule, chocolate_rule)
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

  @patch('bites.Bites.initialise_trail')
  def test_bites_class_can_receive_instance_of_player_class(self, mock_init_trail):
    # test 73
    class FakePlayer():
      pass

    mario = FakePlayer()
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {"chocolate": 0}
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, [mario], anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    self.assertEqual(len(bites_game.players), 2)
    self.assertEqual(bites_game.players[0].name, "mario")
    self.assertEqual(bites_game.players[1].name, "luigi")

  def test_anthill_food_tokens_are_initialised_when_Bites_class_is_instantiated(self):
    # test 118
    ants = []
    standard_tokens_for_trail = {
      "apple": 3,
      "grapes": 3,
      "bread": 3,
      "cheese": 3,
      "pepper": 3}
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)

    expected_anthill_rule_attribute_type = str
    expected_anthill_rule_attribute = anthill_rule

    self.assertEqual(type(bites_game.anthill_rule), expected_anthill_rule_attribute_type)
    self.assertEqual(bites_game.anthill_rule, expected_anthill_rule_attribute)

  def test_Bites_receives_wine_rule_as_string_and_stores_it_as_attribute(self):
    # test 175
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    
    expected_wine_rule_attribute_type = str
    expected_wine_rule_attribute = "test wine rule"

    self.assertEqual(type(bites_game.wine_rule), expected_wine_rule_attribute_type)
    self.assertEqual(bites_game.wine_rule, expected_wine_rule_attribute)

  def test_Bites_receives_chocolate_rule_as_string_and_stores_it_as_attribute(self):
    # test 232
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    
    expected_chocolate_rule_attribute_type = str
    expected_chocolate_rule_attribute = "test chocolate rule"

    self.assertEqual(type(bites_game.chocolate_rule), expected_chocolate_rule_attribute_type)
    self.assertEqual(bites_game.chocolate_rule, expected_chocolate_rule_attribute)

class InitialiseAntsTest(unittest.TestCase):
  def test_can_initialise_one_ant(self):
    # test 1
    ants = ["red"]
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    expected_ant_positions = {"red": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_two_ants(self):
    # test 2
    ants = ["red", "purple"]
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    expected_ant_positions = {"red": None, "purple": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_five_ants(self):
    # test 3
    ants = ["red", "purple", "yellow", "green", "brown"]
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    expected_ant_positions = {
      "red": None,
      "purple": None,
      "yellow": None,
      "green": None,
      "brown": None,}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

class CreatePartialStandardPlusWineTrailTest(unittest.TestCase):
  def test_can_create_partial_trail_of_standard_and_wine_with_one_token(self):
    # test 4
    standard_tokens_for_trail = {"apple": 1}
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    expected_trail = ["apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_create_partial_trail_of_standard_and_wine_with_two_different_tokens(self):
    # test 5
    standard_tokens_for_trail = {"apple": 1, "grapes": 1}
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    expected_trails = [["apple", "grapes"], ["grapes", "apple"]]
    self.assertIn(bites_game.trail, expected_trails)

  def test_can_create_partial_trail_of_standard_and_wine_with_five_of_same_token(self):
    # test 6
    standard_tokens_for_trail = {"apple": 5}
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    expected_trail = ["apple", "apple", "apple", "apple", "apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_shuffle_two_plus_one_tokens(self):
    # test 7
    standard_tokens_for_trail = {"apple": 2, "grapes": 1}
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    wine_tokens_for_trail = {"wine": 5}
    chocolate_tokens_for_trail = {"chocolate": 0}
    ants = []
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    expected_trail_length = 50
    self.assertEqual(len(bites_game.trail), expected_trail_length)
    self.assertEqual(bites_game.trail.count("apple"), 9)
    self.assertEqual(bites_game.trail.count("grapes"), 9)
    self.assertEqual(bites_game.trail.count("cheese"), 9)
    self.assertEqual(bites_game.trail.count("pepper"), 9)
    self.assertEqual(bites_game.trail.count("bread"), 9)
    self.assertEqual(bites_game.trail.count("wine"), 5)

class InitialiseAnthillTest(unittest.TestCase):
  def test_can_initialise_anthill_as_list_with_len_five_and_every_element_is_None(self):
    # test 27
    ants = ['purple', 'red', 'brown', 'yellow', 'green']
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
  
  # @patch('bites.Bites.render_game')
  # def test_one_whole_round_is_played(self, render_game_mock):
  #   # test 76
  #   """
  #   P0 moves brown ant to pos 2 & picks up cheese from behind
  #   P1 moves yellow ant to pos 6 & picks up apple from behind
  #   """
  #   starting_trail = [
  #     "apple", 
  #     "cheese", 
  #     "bread", 
  #     "pepper", 
  #     "grapes", 
  #     "apple", 
  #     "cheese", 
  #     "bread", 
  #     "pepper", 
  #     "grapes"]
  #   starting_ant_positions = {
  #     "red": None,
  #     "yellow": None,
  #     "green": None,
  #     "brown": None,
  #     "purple": None}
  #   starting_anthill = [None, None, None, None, None]
  #   starting_anthill_food_tokens = {}
    
  #   trail_after_turn_1_mario = [
  #     "apple", 
  #     None, 
  #     "bread", 
  #     "pepper", 
  #     "grapes", 
  #     "apple", 
  #     "cheese", 
  #     "bread", 
  #     "pepper", 
  #     "grapes"]
  #   ant_pos_after_turn_1_mario = {
  #     "red": None,
  #     "yellow": None,
  #     "green": None,
  #     "brown": 2,
  #     "purple": None}
  #   anthill_after_turn_1_mario = starting_anthill
  #   anthill_food_tokens_after_turn_1_mario = starting_anthill_food_tokens
    
  #   trail_after_turn_2_luigi = [
  #     "apple", 
  #     None, 
  #     "bread", 
  #     "pepper", 
  #     "grapes", 
  #     None, 
  #     "cheese", 
  #     "bread", 
  #     "pepper", 
  #     "grapes"]
  #   ant_pos_after_turn_2_luigi = {
  #     "red": None,
  #     "yellow": 6,
  #     "green": None,
  #     "brown": 2,
  #     "purple": None}
  #   anthill_after_turn_2_luigi = starting_anthill
  #   anthill_food_tokens_after_turn_2_luigi = starting_anthill_food_tokens
    
  #   expected_new_trail = trail_after_turn_2_luigi
  #   expected_new_ant_positions = ant_pos_after_turn_2_luigi
  #   expected_new_anthill = starting_anthill
  #   expected_new_anthill_food_tokens = starting_anthill_food_tokens
    
  #   fake_mario = mock.MagicMock()
  #   fake_luigi = mock.MagicMock()
  #   players = [fake_mario, fake_luigi]
  #   ants = ["red", "yellow", "green", "brown", "purple"]
  #   standard_tokens_for_trail = {
  #     "cheese": 3, 
  #     "bread": 3,
  #     "grapes": 3,
  #     "apple": 3,
  #     "pepper": 3,
  #     }
  #   wine_tokens_for_trail = {}
  #   chocolate_tokens_for_trail = {}
  #   anthill_rule = ""
  #   wine_rule = ""
  #   chocolate_rule = ""
  #   bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    
  #   bites_game.trail = starting_trail
  #   bites_game.ant_positions = starting_ant_positions
  #   bites_game.anthill = starting_anthill
  #   bites_game.anthill_rule = "top down"
    
  #   fake_mario.take_turn = mock.MagicMock(side_effect = [
  #     (trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, anthill_food_tokens_after_turn_1_mario),
  #     ([], {}, [], {})])
    
  #   fake_luigi.take_turn = mock.MagicMock(return_value = (
  #     trail_after_turn_2_luigi, ant_pos_after_turn_2_luigi, anthill_after_turn_2_luigi, anthill_food_tokens_after_turn_2_luigi))
    
  #   bites_game.take_all_turns()
    
  #   self.assertGreaterEqual(fake_mario.take_turn.call_count, 1)
  #   self.assertEqual(fake_mario.take_turn.call_args_list[0], mock.call(
  #     starting_trail, starting_ant_positions, starting_anthill, bites_game.anthill_rule, starting_anthill_food_tokens))
  #   self.assertGreaterEqual(fake_luigi.take_turn.call_count, 1)
  #   self.assertEqual(fake_luigi.take_turn.call_args_list[0], mock.call(
  #     trail_after_turn_1_mario, ant_pos_after_turn_1_mario, anthill_after_turn_1_mario, bites_game.anthill_rule, anthill_food_tokens_after_turn_1_mario))
  #   self.assertGreaterEqual(render_game_mock.call_count, 3)

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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    fake_mario = mock.MagicMock()
    fake_luigi = mock.MagicMock()
    players = [fake_mario, fake_luigi]
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {"grapes": 1}
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    fake_mario = FakePlayer("mario")
    players = [fake_mario]
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)

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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)

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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    bites_game = Bites([], standard_tokens_for_trail, {}, {}, [], "", "", "")
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

    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    fake_mario = FakePlayer("mario", 3)
    fake_luigi = FakePlayer("luigi", 9)
    players = [fake_mario, fake_luigi]
    bites_game = Bites([], standard_tokens_for_trail, {}, {}, players, "", "", "")
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    bites_game = Bites([], standard_tokens_for_trail, {}, {}, [], "", "", "")
    bites_game.play_full_game()
    expected_calls = [
      mock.call.taking_all_the_turns(), 
      mock.call.printing_the_score()]
    self.assertEqual(manager.mock_calls, expected_calls)

class RenderGameTest(unittest.TestCase):
  @patch('bites.Bites.print_chocolate_rule_statement')
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
    mock_choc_rule_print,
    ):
    # test 183
    manager = mock.Mock()
    manager.attach_mock(mock_wine_rule_print, 'mock_wine_rule_print')
    manager.attach_mock(mock_choc_rule_print, 'mock_choc_rule_print')
    manager.attach_mock(mock_player_details_print, 'mock_player_details_print')
    manager.attach_mock(mock_ants_pre_trail_print, 'mock_ants_pre_trail_print')
    manager.attach_mock(mock_trail_and_ants_print, 'mock_trail_and_ants_print')
    manager.attach_mock(mock_anthill_placement_print, 'mock_anthill_placement_print')
    manager.attach_mock(mock_anthill_food_print, 'mock_anthill_food_print')
    
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = "oenophile"
    chocolate_rule = "doubler"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    bites_game.ant_positions = {"random key": None}

    bites_game.render_game()

    expected_mock_calls = [
      mock.call.mock_wine_rule_print(),
      mock.call.mock_choc_rule_print(),
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
    mock_choc_rule_print.assert_called_once()

  def test_print_players_names_and_hands_prints_player_name_and_hand_for_one_player(self):
    # test 85
    class FakePlayer():
      def __init__(self, name):
        self.name = name
        self.hand = {}

    fake_mario = FakePlayer("mario")
    
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = [fake_mario]
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = [fake_mario]
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = [fake_mario, fake_luigi]
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = "test anthill order"
    wine_rule = "test wine rule"
    chocolate_rule = "test chocolate rule"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = "oenophile"
    chocolate_rule = "doubler"
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
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
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    self.assertIsInstance(bites_game.initialise_anthill_food_tokens(), dict)

  def test_upon_initialisation_anthill_has_one_of_each_type_of_food(self):
    # test 117
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens()), 5)
    self.assertEqual(list(bites_game.initialise_anthill_food_tokens().values()), [1, 1, 1, 1, 1])
    self.assertIn("apple", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("grapes", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("bread", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("cheese", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("pepper", bites_game.initialise_anthill_food_tokens().keys())
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens().keys()), 5)

  @patch('bites.Bites.initialise_trail')
  def test_upon_initialisation_anthill_does_not_have_wine(self, mock_init_trail):
    # test 167
    ants = []
    standard_tokens_for_trail = {
      "apple": 0,
      "grapes": 0,
      "bread": 0,
      "cheese": 0,
      "pepper": 0}
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens()), 5)
    self.assertEqual(list(bites_game.initialise_anthill_food_tokens().values()), [1, 1, 1, 1, 1])
    self.assertIn("apple", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("grapes", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("bread", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("cheese", bites_game.initialise_anthill_food_tokens().keys())
    self.assertIn("pepper", bites_game.initialise_anthill_food_tokens().keys())
    self.assertNotIn("wine", bites_game.initialise_anthill_food_tokens().keys())
    self.assertEqual(len(bites_game.initialise_anthill_food_tokens().keys()), 5)

class IdentifyChocolateLimitTest(unittest.TestCase):
  """Exerpt from the game's official rules:
  The setup should never allow a player to get a chocolate token on the 
  very first turn of the game.

  This is being interpereted as whichever standard food has its first occurence 
  furthest into the trail, that location + 2 is the first place chocolate can be. 
  """
  def test_trail_has_three_cheese_choc_limit_is_2(self):
    # test 184
    ants = []
    standard_tokens_for_trail = {"cheese": 3}
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    bites_game.trail = ["cheese", "cheese", "cheese"]
    expected_chocolate_limit = 2
    actual_chocolate_limit = bites_game.identify_chocolate_limit(bites_game.trail)
    self.assertEqual(actual_chocolate_limit, expected_chocolate_limit)

  def test_trail_has_cheese_bread_cheese_cheese_and_choc_limit_is_3(self):
    # test 185
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      }
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    bites_game.trail = ["cheese", "bread", "cheese", "cheese"]
    expected_chocolate_limit = 3
    actual_chocolate_limit = bites_game.identify_chocolate_limit(bites_game.trail)
    self.assertEqual(actual_chocolate_limit, expected_chocolate_limit)

  def test_trail_has_cheese_cheese_bread_cheese_and_choc_limit_is_4(self):
    # test 186
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      }
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    bites_game.trail = ["cheese", "cheese", "bread", "cheese"]
    expected_chocolate_limit = 4
    actual_chocolate_limit = bites_game.identify_chocolate_limit(bites_game.trail)
    self.assertEqual(actual_chocolate_limit, expected_chocolate_limit)
  
class AddChocolateIntoTrailTest(unittest.TestCase):
  @patch('bites.Bites.identify_chocolate_limit', return_value = 0)
  def test_add_chocolate_calls_shuffle_on_trail(self, mock_choc_lim):
    # test 189
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    bites_game.trail = []
    
    with patch('bites.random.shuffle') as mock_random_shuffle:
      bites_game.add_chocolate_into_trail(bites_game.trail, chocolate_tokens_for_trail)
      mock_random_shuffle.assert_called_once()

  @patch('bites.Bites.identify_chocolate_limit', return_value = 4)
  def test_choc_lim_is_4_and_add_choc_shuffle_does_not_affect_idx_0_to_3_inc(self, mock_choc_lim):
    # test 190
    ants = []
    standard_tokens_for_trail = {"cheese": 0, "bread": 0}
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 1}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    trail = ["cheese", "cheese", "bread", "cheese"]
    expected_new_trail = ["cheese", "cheese", "bread", "cheese", "chocolate"]

    with patch('bites.random.shuffle') as mock_random_shuffle:
      actual_new_trail = bites_game.add_chocolate_into_trail(trail, chocolate_tokens_for_trail)
      mock_random_shuffle.assert_called_once_with(["chocolate"])

    self.assertEqual(actual_new_trail[0], "cheese")
    self.assertEqual(actual_new_trail[1], "cheese")
    self.assertEqual(actual_new_trail[2], "bread")
    self.assertEqual(actual_new_trail[3], "cheese")
    self.assertEqual(actual_new_trail, expected_new_trail)

  @patch('bites.Bites.identify_chocolate_limit', return_value = 9)
  def test_a_typical_example_of_a_game_trail_with_3_of_each_standard_and_2_choc_and_choc_lim_is_8(
    self,
    mock_choc_lim,
    ):
    # test 191
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {"wine": 2}
    chocolate_tokens_for_trail = {"chocolate": 2}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)
    trail = [
      "cheese",
      "grapes",
      "cheese",
      "wine",
      "pepper",
      "cheese",
      "bread",
      "apple",
      "pepper",
      "bread",
      "pepper",
      "bread",
      "grapes",
      "apple",
      "grapes",
      "wine",
      "apple",
      ]
    expected_new_trail_0_to_9 = [
      "cheese",
      "grapes",
      "cheese",
      "wine",
      "pepper",
      "cheese",
      "bread",
      "apple",
      "pepper",
    ]

    with patch('bites.random.shuffle') as mock_random_shuffle:
      actual_new_trail = bites_game.add_chocolate_into_trail(trail, chocolate_tokens_for_trail)
      mock_random_shuffle.assert_called_once_with([
        "bread",
        "pepper",
        "bread",
        "grapes",
        "apple",
        "grapes",
        "wine",
        "apple",
        "chocolate",
        "chocolate",
        ])
    
    self.assertEqual(actual_new_trail[0:9], expected_new_trail_0_to_9)
    self.assertEqual(len(actual_new_trail), 19)
    self.assertEqual(actual_new_trail.count("apple"), 3)
    self.assertEqual(actual_new_trail.count("grapes"), 3)
    self.assertEqual(actual_new_trail.count("cheese"), 3)
    self.assertEqual(actual_new_trail.count("pepper"), 3)
    self.assertEqual(actual_new_trail.count("bread"), 3)
    self.assertEqual(actual_new_trail.count("chocolate"), 2)
    self.assertEqual(actual_new_trail.count("wine"), 2)

  @patch('bites.Bites.identify_chocolate_limit', return_value = 8)
  @patch('bites.Bites.__init__', return_value = None)
  def test_what_happens_if_there_is_more_than_one_type_of_choc(
    self,
    mock_bites_init,
    mock_choc_lim,
    ):
    # test 194
    chocolate_tokens_for_trail = {"white choc": 2, "dark choc": 3}

    bites_game = Bites()
    partial_trail = [
      "cheese",
      "grapes",
      "cheese",
      "pepper",
      "cheese",
      "bread",
      "apple",
      "pepper",
      "bread",
      "pepper",
      "bread",
      "grapes",
      "apple",
      "grapes",
      "apple",
      ]

    bites_game.trail = bites_game.add_chocolate_into_trail(partial_trail, chocolate_tokens_for_trail)

    self.assertEqual(bites_game.trail[0:8], partial_trail[0:8])
    self.assertEqual(len(bites_game.trail), 20)
    self.assertEqual(bites_game.trail.count("white choc"), bites_game.trail[8:].count("white choc"))
    self.assertEqual(bites_game.trail.count("dark choc"), bites_game.trail[8:].count("dark choc"))
    self.assertNotEqual(bites_game.trail[-5:], ["white choc", "white choc", "dark choc", "dark choc", "dark choc"])

class InitialiseTrailTest(unittest.TestCase):
  @patch('bites.Bites.add_chocolate_into_trail')
  def test_initialise_trail_calls_create_partial_trail(self, mock_add_choc):
    # test 192
    ants = []
    standard_tokens_for_trail = {
      "cheese": 3, 
      "bread": 3,
      "grapes": 3,
      "apple": 3,
      "pepper": 3,
      }
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    players = []
    anthill_rule = ""
    wine_rule = ""
    chocolate_rule = ""
    bites_game = Bites(ants, standard_tokens_for_trail, wine_tokens_for_trail, chocolate_tokens_for_trail, players, anthill_rule, wine_rule, chocolate_rule)

    """Using context-manager rather than decorator because method is called once 
    during __init__ and a second time manually. The test assertions are refering to 
    the manual call.
    """
    with patch('bites.Bites.create_partial_trail_of_standard_and_wine') as mock_create_partial:
      trail = bites_game.initialise_trail(wine_tokens_for_trail, chocolate_tokens_for_trail)
      mock_create_partial.assert_called_once_with(wine_tokens_for_trail)

  @patch('bites.Bites.__init__', return_value = None)
  @patch('bites.Bites.add_chocolate_into_trail', 
    return_value = ["bread", "cheese", "bread", "chocolate",])
  @patch('bites.Bites.create_partial_trail_of_standard_and_wine', 
    return_value = ["bread", "cheese", "bread",])
  def test_initialise_trail_calls_add_chocolate(
    self, 
    mock_create_partial,
    mock_add_choc,
    mock_bites_init
    ):
    # test 193
    wine_tokens_for_trail = {"wine": 0}
    chocolate_tokens_for_trail = {"chocolate": 0}
    
    bites_game = Bites()
    
    trail = bites_game.initialise_trail(wine_tokens_for_trail, chocolate_tokens_for_trail)
    mock_add_choc.assert_called_once_with(["bread", "cheese", "bread"], chocolate_tokens_for_trail)
    self.assertEqual(trail, ["bread", "cheese", "bread", "chocolate"])

if __name__ == '__main__':
  unittest.main(verbosity = 2)
