from unittest import TestCase

from exercises.python.list.list_generator import list_generator


class Test(TestCase):
    def test_list_generator(self):
        self.assertEqual(['34', '67', '55', '33', '12', '98'], list_generator('34,67,55,33,12,98'))
