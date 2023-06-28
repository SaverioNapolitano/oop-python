from unittest import TestCase

from exercises.python.iterativestatements.fibonacci import fibonacci


class Test(TestCase):
    def test_fibonacci(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8], fibonacci(10))
        self.assertEqual([0, 1, 1, 2, 3], fibonacci(3))
