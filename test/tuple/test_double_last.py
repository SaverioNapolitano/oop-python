from unittest import TestCase

from exercises.python.tuple.double_last import double_last


class Test(TestCase):
    def test_double(self):
        self.assertEqual([(10, 20, 80), (40, 50, 120), (70, 80, 180)], double_last([(10, 20, 40), (40, 50, 60), (70, 80, 90)]))
        self.assertEqual([(10, 80), (40, 120), (70, 180)],
                         double_last([(10, 40), (40, 60), (70, 90)]))
