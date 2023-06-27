from unittest import TestCase

from exercises.python.strings.remove_char import remove_char


class Test(TestCase):
    def test_remove_char(self):
        self.assertEqual('tet', remove_char('test', 2))
        self.assertIsNone(remove_char(12, 1))
        self.assertIsNone(remove_char('abc', 4))
        self.assertIsNone(remove_char('', 0))
