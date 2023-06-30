from unittest import TestCase

from exercises.python.tuple.get_4 import get_4


class Test(TestCase):
    def test_get_4(self):
        self.assertEqual((4, 3), get_4((1, 2, 3, 4, 5, 6)))
        self.assertEqual(('d', 'c'), get_4(('a', 'b', 'c', 'd', 'e', 'f')))
        self.assertIsNone(get_4([1, 2, 3, 4]))
