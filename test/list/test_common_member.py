from unittest import TestCase

from exercises.python.list.common_member import common_member


class Test(TestCase):
    def test_common_member(self):
        self.assertTrue(common_member([1, 2, 3], ['a', 4, 1]))
        self.assertFalse(common_member(['1', '2', 3], [1, 2, '3']))
