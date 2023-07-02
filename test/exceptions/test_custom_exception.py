from unittest import TestCase

from exercises.python.exceptions.custom_exception import CustomException


class TestCustomException(TestCase):
    def test_invoke(self):
        self.assertRaises(CustomException, CustomException('Custom Exception').invoke)
