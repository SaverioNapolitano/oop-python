from unittest import TestCase

from exercises.python.list.double import double


class Test(TestCase):
    def test_double(self):
        self.assertEqual([2, 4, 6], double([1, 2, 3]))
        self.assertEqual(['aa', 'bb', 'cc'], double(['a', 'b', 'c']))
