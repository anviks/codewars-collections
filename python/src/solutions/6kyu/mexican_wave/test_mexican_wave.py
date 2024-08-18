"""https://www.codewars.com/kata/58f5c63f1e26ecda7e000029"""

import pytest

from solution_mexican_wave import wave


@pytest.mark.parametrize('string, expected', [
    ("hello", ["Hello", "hEllo", "heLlo", "helLo", "hellO"]),
    ("codewars", ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]),
    ("", []),
    ("two words", ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs",
                   "two wordS"]),
    (" gap ", [" Gap ", " gAp ", " gaP "]),
    ("a       b    ", ["A       b    ", "a       B    "]),
    ("this is a few words",
     ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words",
      "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words",
      "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds",
      "this is a few woRds", "this is a few worDs", "this is a few wordS"])
])
def test_should_return_join_result(string, expected):
    assert wave(string) == expected
