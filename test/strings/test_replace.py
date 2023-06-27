from unittest import TestCase

from exercises.python.strings.replace import replace


class Test(TestCase):
    def test_replace(self):
        self.assertEqual('I like cats and birds, but I\'d much rather own a bird.', replace())
