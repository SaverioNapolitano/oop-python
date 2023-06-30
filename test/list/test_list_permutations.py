from unittest import TestCase

from exercises.python.list.list_permutations import list_permutations


class Test(TestCase):
    def test_list_permutations(self):
        self.assertIsNone(list_permutations([1, 2, 3]))
