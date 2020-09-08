import unittest
from player import Player

class InitTest(unittest.TestCase):
  def test___init___method_works(self):
  # test 30
  # This test was written rertrospectively; the __init__ method came about 
  # naturally during refactoring of the code into the Player class.
    mario = Player("placeholder name")
    expected_mario_hand = {}
    expected_mario_score = 0
    self.assertIsInstance(mario, Player)
    self.assertEqual(mario.hand, expected_mario_hand)
    self.assertEqual(mario.score, expected_mario_score)

  def test_player_instance_has_name(self):
  # test 31
    mario = Player("Mario Mario")
    expected_name = "Mario Mario"
    self.assertEqual(mario.name, "Mario Mario")

class InitialiseHandTest(unittest.TestCase):
  def test_can_initialise_player_hand(self):
  # test 9
    mario = Player("placeholder name")
    # hand = initialise_hand()
    self.assertIsInstance(mario.hand, dict)
    self.assertEqual(len(mario.hand), 0)

class StoreFoodTest(unittest.TestCase):
  def test_can_receive_single_food_to_empty_hand(self):
  # test 19
    mario = Player("placeholder name")
    food = "apple"
    expected_new_hand = {"apple": 1}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)

  def test_can_receive_second_token_of_same_food(self):
  # test 20
    mario = Player("placeholder name")
    mario.hand = {"apple": 1}
    food = "apple"
    expected_new_hand = {"apple": 2}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)

  def test_can_receive_food_not_already_in_hand(self):
    # test 21
      mario = Player("placeholder name")
      mario.hand = {"apple": 2}
      food = "cheese"
      expected_new_hand = {"apple": 2, "cheese": 1}
      mario.store_food(food)
      self.assertEqual(mario.hand, expected_new_hand)

class ScoreHandTest(unittest.TestCase):
  def test_can_score_four_points_for_one_token_in_top_slot(self):
  # test 22
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"pepper": 1}
    expected_score = 4
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_three_points_for_one_token_in_second_top_slot(self):
  # test 23
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"bread": 1}
    expected_score = 3
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_four_points_for_two_tokens_in_middle_slot(self):
  # test 24
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {"cheese": 2}
    expected_score = 4
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_ten_points_for_one_of_each_token(self):
  # test 25
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {
      "apple": 1,
      "grapes": 1,
      "cheese": 1,
      "bread": 1,
      "pepper": 1}
    expected_score = 10
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_can_score_twenty_points_for_two_of_each_token(self):
  # test 26
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {
      "apple": 2,
      "grapes": 2,
      "cheese": 2,
      "bread": 2,
      "pepper": 2}
    expected_score = 20
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_typical_end_of_game_hand_gives_correct_score(self):
  # test 28
    mario = Player("placeholder name")
    anthill = ["red", "purple", "yellow", "brown", "green"]
    mario.hand = {
      "apple": 3,
      "grapes": 4,
      "cheese": 0,
      "bread": 1,
      "pepper": 2}
    expected_score = 15
    mario.score_hand(anthill)
    self.assertEqual(mario.score, expected_score)

  def test_same_hand_gives_different_scores_for_different_anthill_configurations(self):
  # test 29
    mario = Player("placeholder name")
    luigi = Player("placeholder name")
    anthill_a = ["red", "purple", "yellow", "brown", "green"]
    anthill_b = ["purple", "yellow", "brown", "red", "green"]
    hand = {
      "apple": 3,
      "grapes": 4,
      "cheese": 0,
      "bread": 1,
      "pepper": 2}
    mario.hand = hand
    luigi.hand = hand
    expected_score_a = 15
    expected_score_b = 19
    mario.score_hand(anthill_a)
    luigi.score_hand(anthill_b)
    self.assertNotEqual(mario.score, luigi.score)
    self.assertEqual(mario.score, expected_score_a)
    self.assertEqual(luigi.score, expected_score_b)















if __name__ == '__main__':
  unittest.main()
