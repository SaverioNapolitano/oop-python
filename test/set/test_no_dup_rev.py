from unittest import TestCase

from exercises.python.set.no_dup_rev import no_dup_rev


class Test(TestCase):
    def test_no_dup_rev(self):
        self.assertEqual([155, 120, 88, 24, 35, 12], no_dup_rev([12, 24, 35, 24, 88, 120, 155, 88, 120, 155]))
