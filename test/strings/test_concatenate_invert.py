from unittest import TestCase

from exercises.python.strings.concatenate_invert import concatenate_invert


class Test(TestCase):
    def test_concatenate_invert(self):
        self.assertEqual('xyc abz', concatenate_invert('abc', 'xyz'))
        self.assertIsNone(concatenate_invert(453, 126))
