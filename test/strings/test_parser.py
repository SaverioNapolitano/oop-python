from unittest import TestCase

from exercises.python.strings.parser import parser


class Test(TestCase):
    def test_parser(self):
        self.assertEqual('abcing', parser('abc'))
        self.assertEqual('stringly', parser('string'))

