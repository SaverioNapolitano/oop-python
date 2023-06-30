from unittest import TestCase

from exercises.python.list.list_product import list_product


class Test(TestCase):
    def test_list_product(self):
        self.assertEqual(['a', 'bb', 'ccc'], list_product([1, 2, 3], ['a', 'b', 'c']))
        self.assertEqual([1, 4, 9], list_product([1, 2, 3], [1, 2, 3]))
