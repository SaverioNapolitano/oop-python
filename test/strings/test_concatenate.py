from unittest import TestCase

from exercises.python.strings.concatenate import concatenate


class Test(TestCase):
    def test_concatenate(self):
        self.assertEqual('ab', concatenate('a', 'b'))
        self.assertEqual('12', concatenate(1, 2))
        self.assertEqual('1.22.3', concatenate(1.2, 2.3))
