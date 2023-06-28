from unittest import TestCase

from exercises.python.iterativestatements.factorial import factorial


class Test(TestCase):
    def test_factorial(self):
        self.assertEqual(120, factorial(5))
        self.assertEqual(1, factorial(0))
        self.assertIsNone(factorial(1.5))
