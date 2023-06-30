from unittest import TestCase

from exercises.python.dictionary.phonebook import phonebook


class Test(TestCase):
    def test_phonebook(self):
        self.assertIsNone(phonebook())
