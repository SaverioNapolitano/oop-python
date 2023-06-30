from unittest import TestCase

from exercises.python.tuple.convert import convert


class Test(TestCase):
    def test_convert(self):
        self.assertEqual([1, 2, 3], convert((1, 2, 3)))
        self.assertEqual(['a', 2, 'c'], convert(('a', 2, 'c')))
