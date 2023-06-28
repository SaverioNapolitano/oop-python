from unittest import TestCase

from exercises.python.conditionalstatements.max_length import max_length


class Test(TestCase):
    def test_max_length(self):
        self.assertIsNone(max_length('abc', 'test'))
        self.assertIsNone(max_length('test', 'abc'))
        self.assertIsNone(max_length('hello', 'there'))
