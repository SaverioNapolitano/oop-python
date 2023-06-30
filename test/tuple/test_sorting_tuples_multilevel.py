from unittest import TestCase

from exercises.python.tuple.sorting_tuples_multilevel import sorting_tuples_multilevel


class Test(TestCase):
    def test_sorting_tuples_multilevel(self):
        self.assertEqual([('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93),
                          ('Json', 21, 85), ('Tom', 19, 80)],
                         sorting_tuples_multilevel([('Tom', 19, 80), ('John', 20, 90), ('Jony', 17, 91),
                                                    ('Jony', 17, 93), ('Json', 21, 85)]))
