from unittest import TestCase

from exercises.python.strings.reverse import reverse


class Test(TestCase):
    def test_reverse(self):
        self.assertEqual('tset', reverse('test'))
        self.assertEqual('tests', reverse('tests'))
        self.assertEqual(12, reverse(12))
