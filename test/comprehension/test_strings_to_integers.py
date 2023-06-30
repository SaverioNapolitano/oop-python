from unittest import TestCase

from exercises.python.comprehension.strings_to_integers import strings_to_integers


class Test(TestCase):
    def test_strings_to_integers(self):
        self.assertEqual([1, 2, 3], strings_to_integers(['a', 'ab', 'abc']))
