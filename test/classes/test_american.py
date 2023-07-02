from unittest import TestCase

from exercises.python.classes.american import American


class TestAmerican(TestCase):
    def test_get_nationality(self):
        self.assertEqual('American', American.get_nationality())
