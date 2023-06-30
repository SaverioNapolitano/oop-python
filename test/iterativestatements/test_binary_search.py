from unittest import TestCase

from exercises.python.iterativestatements.binary_search import binary_search


class Test(TestCase):
    def test_binary_search(self):
        self.assertEqual(-1, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))
        self.assertEqual(1, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
        self.assertEqual(2, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
        self.assertEqual(8, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
