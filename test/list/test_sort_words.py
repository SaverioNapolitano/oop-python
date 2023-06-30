from unittest import TestCase

from exercises.python.list.sort_words import sort_words


class Test(TestCase):
    def test_sort_words(self):
        self.assertEqual('bag,hello,without,world', sort_words('without,hello,bag,world'))
