from unittest import TestCase

from exercises.python.comprehension.remove_indexes import remove_indexes


class Test(TestCase):
    def test_remove_indexes(self):
        self.assertEqual([24, 70, 120], remove_indexes([12, 24, 35, 70, 88, 120, 155]))
