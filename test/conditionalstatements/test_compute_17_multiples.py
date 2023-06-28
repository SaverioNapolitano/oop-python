from unittest import TestCase

from exercises.python.conditionalstatements.compute_17_multiples import compute_17_multiples


class Test(TestCase):
    def test_compute_17_multiples(self):
        self.assertEqual(17, compute_17_multiples())
