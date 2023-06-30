from unittest import TestCase

from exercises.python.comprehension.sort_words_no_dup import sort_words_no_dup


class Test(TestCase):
    def test_sort_words_no_dup(self):
        self.assertEqual('again and hello makes perfect practice world',
                         sort_words_no_dup('hello world and practice makes perfect and hello world again'))
