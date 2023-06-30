from unittest import TestCase

from exercises.python.tuple.sorting_tuples import sorting_tuples


class Test(TestCase):
    def test_sorting_tuples(self):
        self.assertEqual([(3, 4, 1), (0, 5, 2), (6, 7, 8)], sorting_tuples([(0, 5, 2), (3, 4, 1), (6, 7, 8)]))
        self.assertEqual([('j', 'a', 'z'), ('b', 'c', 'h'), ('a', 'f', 'd')],
                         sorting_tuples([('a', 'f', 'd'), ('b', 'c', 'h'), ('j', 'a', 'z')]))
