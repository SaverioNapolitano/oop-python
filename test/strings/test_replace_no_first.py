from unittest import TestCase

from exercises.python.strings.replace_no_first import replace_no_first


class Test(TestCase):
    def test_replace_no_first(self):
        self.assertEqual('resta$t', replace_no_first('restart'))
        self.assertIsNone(replace_no_first(121))
