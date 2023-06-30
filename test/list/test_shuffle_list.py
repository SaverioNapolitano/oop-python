from unittest import TestCase

from exercises.python.list.shuffle_list import shuffle_list


class Test(TestCase):
    def test_shuffle_list(self):
        self.assertIsNone(shuffle_list([3, 6, 7, 8]))
