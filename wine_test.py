import wine
import unittest
from player import Player

class ScoreWineOenophileMethodTest(unittest.TestCase):
  def test_score_wine_Oenophile_method_returns_int(self):
    # test 168
    mario = Player("Mario")
    mario.hand = {"wine": 0}
    standard_tokens_for_trail = {"apple": 0}
    actual_result = wine.score_wine_Oenophile_method(mario.hand, standard_tokens_for_trail)
    self.assertIsInstance(actual_result, int)

  def test_one_wine_in_hand__wine_Oenophile_score_is_1(self):
    # test 169
    mario = Player("Mario")
    standard_tokens_for_trail = {"apple": 0}
    mario.hand = {"wine": 1}
    expected_result = 1
    actual_result = wine.score_wine_Oenophile_method(mario.hand, standard_tokens_for_trail)
    self.assertEqual(actual_result, expected_result)

  def test_two_wines_in_hand__wine_Oenophile_score_is_4(self):
    # test 170
    mario = Player("Mario")
    standard_tokens_for_trail = {"apple": 0}
    mario.hand = {"wine": 2}
    expected_result = 4
    actual_result = wine.score_wine_Oenophile_method(mario.hand, standard_tokens_for_trail)
    self.assertEqual(actual_result, expected_result)

class ScoreWineCollectorMethodTest(unittest.TestCase):
  def test_score_wine_Collector_method_returns_int(self):
    # test 158
    mario = Player("Mario")
    mario.hand = {"wine": 0}
    standard_tokens_for_trail = {"apple": 0}
    actual_result = wine.score_wine_Collector_method(mario.hand, standard_tokens_for_trail)
    self.assertIsInstance(actual_result, int)

  def test_one_wine_and_one_standard_food__wine_Collector_score_is_1(self):
    # test 159
    mario = Player("Mario")
    standard_tokens_for_trail = {"apple": 0}
    mario.hand = {"apple": 1, "wine": 1}
    expected_result = 1
    actual_result = wine.score_wine_Collector_method(mario.hand, standard_tokens_for_trail)
    self.assertEqual(actual_result, expected_result)

  def test_two_wines_and_one_standard_food__wine_Collector_score_is_2(self):
    # test 160
    mario = Player("Mario")
    standard_tokens_for_trail = {"apple": 0}
    mario.hand = {"apple": 1, "wine": 2}
    expected_result = 2
    actual_result = wine.score_wine_Collector_method(mario.hand, standard_tokens_for_trail)
    self.assertEqual(actual_result, expected_result)

  def test_two_wines_and_two_different_standard_foods__wine_Collector_score_is_4(self):
    # test 161
    mario = Player("Mario")
    standard_tokens_for_trail = {"apple": 0, "grapes": 0}
    mario.hand = {"apple": 1, "grapes": 1, "wine": 2}
    expected_result = 4
    actual_result = wine.score_wine_Collector_method(mario.hand, standard_tokens_for_trail)
    self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
  unittest.main(verbosity = 2)
