from unittest import TestCase

from exercises.python.classes.person import Female


class TestFemale(TestCase):
    def test_get_gender(self):
        self.assertEqual('Female', Female().get_gender())
