from unittest import TestCase

from exercises.python.conditionalstatements.is_even import is_even


class Test(TestCase):
    def test_is_even(self):
        self.assertIsNone(is_even(2))
        self.assertIsNone(is_even(3))
