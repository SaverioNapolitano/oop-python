from unittest import TestCase

from exercises.python.tuple.sorting_list_string import sorting_list_string


class Test(TestCase):
    def test_sorting_list_string(self):
        self.assertEqual(['wow', 'test', 'hello', 'abc'], sorting_list_string(['test', 'hello', 'abc', 'wow']))
