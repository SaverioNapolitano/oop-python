from unittest import TestCase

from exercises.python.classes.person import Male


class TestMale(TestCase):
    def test_get_gender(self):
        self.assertEqual('Male', Male().get_gender())
