from unittest import TestCase

from exercises.python.dictionary.count_alpha import count_alpha


class Test(TestCase):
    def test_count_alpha(self):
        self.assertEqual({'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}, count_alpha('Hello World!'))
