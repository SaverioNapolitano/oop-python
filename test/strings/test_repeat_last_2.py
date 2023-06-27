from unittest import TestCase

from exercises.python.strings.repeat_last_2 import repeat_last_2


class Test(TestCase):
    def test_repeat_last_2(self):
        self.assertEqual('onononon', repeat_last_2('Python'))
        self.assertEqual('eseseses', repeat_last_2('Exercises'))
        self.assertIsNone(repeat_last_2('a'))
