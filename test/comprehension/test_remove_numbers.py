from unittest import TestCase

from exercises.python.comprehension.remove_numbers import remove_numbers


class Test(TestCase):
    def test_remove_numbers(self):
        self.assertEqual([12, 24, 88, 120, 155], remove_numbers([12, 24, 35, 70, 88, 120, 155]))
