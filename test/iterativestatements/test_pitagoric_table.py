from unittest import TestCase

from exercises.python.iterativestatements.pitagoric_table import pitagoric_table


class Test(TestCase):
    def test_pitagoric_table(self):
        self.assertIsNone(pitagoric_table())
