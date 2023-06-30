from unittest import TestCase

from exercises.python.set.intersect import intersect


class Test(TestCase):
    def test_list_intersect(self):
        self.assertEqual([35], intersect([1, 3, 6, 78, 35, 55], [12, 24, 35, 24, 88, 120, 155]))
