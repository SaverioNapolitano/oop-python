from unittest import TestCase

from exercises.python.strings.is_password_valid import is_password_valid


class Test(TestCase):
    def test_is_password_valid(self):
        self.assertEqual(True, is_password_valid('12345678'))
        self.assertEqual(False, is_password_valid('password'))
        self.assertEqual(False, is_password_valid(12345678))
        self.assertEqual(False, is_password_valid('p455w0rd'))
