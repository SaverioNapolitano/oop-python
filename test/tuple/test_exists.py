from unittest import TestCase

from exercises.python.tuple.exists import exists


class Test(TestCase):
    def test_exists(self):
        self.assertTrue(exists([1, 2, 3], 1))
        self.assertFalse(exists([1, 2, 3], 4))
        self.assertTrue(exists(['a', 'b', 'c'], 'a'))
        self.assertFalse(exists(['1', 2, '3'], 3))
