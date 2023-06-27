from unittest import TestCase

from exercises.python.strings.even_index import even_index


class Test(TestCase):
    def test_even_index(self):
        self.assertIsNone(even_index())
