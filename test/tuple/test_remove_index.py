from unittest import TestCase

from exercises.python.tuple.remove_index import remove_index


class Test(TestCase):
    def test_remove_index(self):
        self.assertEqual((1, 2, 3, 5), remove_index((1, 2, 3, 4, 5), 3))
        self.assertEqual(('a', 'b', 'c'), remove_index(('a', 'b', 'c'), 5))
