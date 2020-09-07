import unittest
from player import Player

class InitialiseHandTest(unittest.TestCase):
  def test_can_initialise_player_hand(self):
  # test 9
    mario = Player()
    # hand = initialise_hand()
    self.assertIsInstance(mario.hand, dict)
    self.assertEqual(len(mario.hand), 0)


class StoreFoodTest(unittest.TestCase):
  def test_can_receive_single_food_to_empty_hand(self):
  # test 19
    mario = Player()
    food = "apple"
    expected_new_hand = {"apple": 1}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)

  def test_can_receive_second_token_of_same_food(self):
  # test 20
    mario = Player()
    mario.hand = {"apple": 1}
    food = "apple"
    expected_new_hand = {"apple": 2}
    mario.store_food(food)
    self.assertEqual(mario.hand, expected_new_hand)

















if __name__ == '__main__':
  unittest.main()
