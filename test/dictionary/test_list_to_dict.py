from unittest import TestCase

from exercises.python.dictionary.list_to_dict import list_to_dict


class Test(TestCase):
    def test_list_to_dict(self):
        self.assertEqual({'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'},
                         list_to_dict(['red', 'green', 'blue'], ['#FF0000', '#008000', '#0000FF']))
