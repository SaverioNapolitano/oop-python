from unittest import TestCase

from exercises.python.strings.split import split


class Test(TestCase):
    def test_split(self):
        self.assertEqual(['I\'m using a test', 'string'], split('I\'m using a test string', None))
        self.assertEqual(['Now', 'I change the delimiter'], split('Now, I change the delimiter', ', '))
        self.assertIsNone(split(1.2, '.'))

