import unittest
from bites import Bites
# from bites import

class BitesInitTest(unittest.TestCase):
  def test___init___method_works(self):
  # test 36
  # This test was written rertrospectively; the __init__ method came about 
  # naturally during refactoring of the code into the Bites class.
    test_ants = ['purple', 'yellow']
    test_tokens = {
      'grapes': 1,
      'cheese': 1}
    bites_game = Bites(test_ants, test_tokens)
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

class InitialiseAntsTest(unittest.TestCase):
  # test 1
  def test_can_initialise_one_ant(self):
    ants = ["red"]
    tokens_for_trail = {}
    bites_game = Bites(ants, tokens_for_trail)
    expected_ant_positions = {"red": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_two_ants(self):
  # test 2
    ants = ["red", "purple"]
    tokens_for_trail = {}
    bites_game = Bites(ants, tokens_for_trail)
    expected_ant_positions = {"red": None, "purple": None}
    self.assertEqual(bites_game.ant_positions, expected_ant_positions)

  def test_can_initialise_five_ants(self):
  # test 3
    ants = ["red", "purple", "yellow", "green", "brown"]
    tokens_for_trail = {}
    bites_game = Bites(ants, tokens_for_trail)
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
    bites_game = Bites(ants, foods)
    expected_trail = ["apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_initialise_trail_with_two_different_tokens(self):
  # test 5
    foods = {"apple": 1, "grapes": 1}
    ants = []
    bites_game = Bites(ants, foods)
    expected_trails = [["apple", "grapes"], ["grapes", "apple"]]
    self.assertIn(bites_game.trail, expected_trails)

  def test_can_initialise_trail_with_five_of_same_token(self):
  # test 6
    foods = {"apple": 5}
    ants = []
    bites_game = Bites(ants, foods)
    expected_trail = ["apple", "apple", "apple", "apple", "apple"]
    self.assertEqual(bites_game.trail, expected_trail)

  def test_can_shuffle_two_plus_one_tokens(self):
  # test 7
    foods = {"apple": 2, "grapes": 1}
    ants = []
    bites_game = Bites(ants, foods)
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
    bites_game = Bites(ants, foods)
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
    bites_game = Bites(ants, tokens_for_trail)
    expected_anthill = [None, None, None, None, None]
    self.assertEqual(bites_game.anthill, expected_anthill)

class ToBeReassignedTest(unittest.TestCase):
  def test_bites_class_can_receive_instance_of_player_class(self):
  # test 73
    class FakePlayer():
      pass

    mario = FakePlayer()
    ants = []
    tokens_for_trail = {}
    play_bites = Bites(ants, tokens_for_trail, [mario])

    self.assertIsInstance(play_bites.players[0], FakePlayer)

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
    play_bites = Bites(ants, tokens_for_trail, players)

    self.assertEqual(len(play_bites.players), 2)
    self.assertEqual(play_bites.players[0].name, "mario")
    self.assertEqual(play_bites.players[1].name, "luigi")

  def test_first_player_takes_one_turn(self):
  # test 75
    class FakePlayer():
      def __init__(self):
        self.callback = []

      def take_turn(self, trail, ant_positions, anthill):
        self.callback.append("take turn")
        new_trail = ["apple", None]
        new_ant_positions = {
          "red": 0,
          "yellow": None,
          "green": None,
          "brown": None,
          "purple": None}
        new_anthill = [None, None, None, None, None]
        return (new_trail, new_ant_positions, new_anthill)

    players = [FakePlayer(), FakePlayer()]
    ants = ["red", "yellow", "green", "brown", "purple"]
    tokens_for_trail = {}
    bites_game = Bites(ants, tokens_for_trail, players)
    bites_game.trail = ["apple", "apple"]
    bites_game.ant_positions = {
      "red": None,
      "yellow": None,
      "green": None,
      "brown": None,
      "purple": None}

    bites_game.play()

    self.assertEqual(bites_game.players[0].callback, ["take turn"])
    self.assertEqual(bites_game.players[1].callback, [])
    self.assertEqual(bites_game.trail, ["apple", None])
    self.assertEqual(bites_game.ant_positions, {
          "red": 0,
          "yellow": None,
          "green": None,
          "brown": None,
          "purple": None})
    self.assertEqual(bites_game.anthill, [None, None, None, None, None])









if __name__ == '__main__':
  unittest.main()
