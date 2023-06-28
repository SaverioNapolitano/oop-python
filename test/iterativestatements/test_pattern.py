from unittest import TestCase

from exercises.python.iterativestatements.pattern import pattern


class Test(TestCase):
    def test_pattern(self):
        self.assertIsNone(pattern())
