from unittest import TestCase

from exercises.python.classes.person import Person


class TestPerson(TestCase):
    def test_gender(self):
        self.assertEqual('Unknown', Person().get_gender())
