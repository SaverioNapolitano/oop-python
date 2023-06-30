from unittest import TestCase

from exercises.python.dictionary.square import square


class Test(TestCase):
    def test_square(self):
        self.assertEqual({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144,
                          13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}, square())
