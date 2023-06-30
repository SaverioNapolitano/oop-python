from unittest import TestCase

from exercises.python.comprehension.lengths import lengths


class Test(TestCase):
    def test_lengths(self):
        self.assertIsNone(lengths())
