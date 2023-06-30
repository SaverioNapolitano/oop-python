from unittest import TestCase

from exercises.python.comprehension.filter_odd import filter_odd


class Test(TestCase):
    def test_filter_odd(self):
        self.assertEqual([1, 3, 5, 7, 9], filter_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))
