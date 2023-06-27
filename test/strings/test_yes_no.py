from unittest import TestCase

from exercises.python.strings.yes_no import yes_no


class Test(TestCase):
    def test_yes_no(self):
        self.assertIsNone(yes_no('YeS'))
        self.assertIsNone(yes_no('YeSsA'))
        self.assertIsNone(yes_no(42))
