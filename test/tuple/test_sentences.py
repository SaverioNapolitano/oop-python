from unittest import TestCase

from exercises.python.tuple.sentences import sentences


class Test(TestCase):
    def test_sentences(self):
        self.assertIsNone(sentences())
