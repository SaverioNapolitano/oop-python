from unittest import TestCase

from exercises.python.strings.first_2_last_2 import first_2_last_2


class Test(TestCase):
    def test_first_2_last_2(self):
        self.assertEqual('w3ce', first_2_last_2('w3resource'))
        self.assertEqual('w3w3', first_2_last_2('w3'))
        self.assertEqual('', first_2_last_2('a'))
        self.assertEqual('', first_2_last_2(2))