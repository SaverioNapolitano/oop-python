from unittest import TestCase

from exercises.python.dictionary.person import person


class Test(TestCase):
    def test_person(self):
        self.assertIsNone(person())
