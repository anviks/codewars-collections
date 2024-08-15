"""https://www.codewars.com/kata/58f5c63f1e26ecda7e000029"""

import unittest

from solution import wave


class Testing(unittest.TestCase):
    def test_should_return_join_result(self):
        result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
        self.assertEqual(wave("hello"), result)

    def test_should_return_join_result2(self):
        result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
        self.assertEqual(wave("codewars"), result)

    def test_should_return_join_result3(self):
        result = []
        self.assertEqual(wave(""), result)

    def test_should_return_join_result4(self):
        result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs",
                  "two wordS"]
        self.assertEqual(wave("two words"), result)

    def test_should_return_join_result5(self):
        result = [" Gap ", " gAp ", " gaP "]
        self.assertEqual(wave(" gap "), result)

    def test_should_return_join_result6(self):
        result = ["A       b    ", "a       B    "]
        self.assertEqual(wave("a       b    "), result)

    def test_should_return_join_result7(self):
        result = ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words",
                  "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words",
                  "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds",
                  "this is a few woRds", "this is a few worDs", "this is a few wordS"]
        self.assertEqual(wave("this is a few words"), result)
