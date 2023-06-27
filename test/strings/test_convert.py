from unittest import TestCase

from exercises.python.strings.convert import convert


class Test(TestCase):
    def test_convert(self):
        self.assertEqual('10', convert(10))
