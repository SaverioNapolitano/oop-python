from unittest import TestCase

from exercises.python.iterativestatements.dice_game import dice_game


class Test(TestCase):
    def test_dice_game(self):
        self.assertIsNone(dice_game())
