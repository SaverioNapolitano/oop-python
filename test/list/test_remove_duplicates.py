from unittest import TestCase

from exercises.python.list.remove_duplicates import remove_duplicates


class Test(TestCase):
    def test_remove_duplicates(self):
        self.assertEqual([1, 2, 3], remove_duplicates([1, 2, 2, 1, 3, 3]))
