from unittest import TestCase

from exercises.python.exceptions.runtime_exception import runtime_exception


class Test(TestCase):
    def test_runtime_exception(self):
        self.assertRaises(RuntimeError, runtime_exception)
