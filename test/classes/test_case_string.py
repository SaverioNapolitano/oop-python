from unittest import TestCase

from exercises.python.classes.case_string import CaseString


class TestCaseString(TestCase):
    def test_set_upper(self):
        case_string = CaseString('test', False)
        case_string.set_upper(True)
        self.assertEqual('TEST', case_string.get_string())
        case_string = CaseString('test', True)
        case_string.set_upper(False)
        self.assertEqual('test', case_string.get_string())
