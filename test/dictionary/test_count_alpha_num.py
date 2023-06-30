from unittest import TestCase

from exercises.python.dictionary.count_alpha_num import count_alpha_num


class Test(TestCase):
    def test_count_alpha_num(self):
        self.assertEqual({'digits': 3, 'letters': 10}, count_alpha_num('hello world! 123'))
