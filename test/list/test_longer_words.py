from unittest import TestCase

from exercises.python.list.longer_words import longer_words


class Test(TestCase):
    def test_longer_words(self):
        self.assertEqual(['hello', 'Python'], longer_words(['test', 'abc', 'hello', 'Python'], 4))
