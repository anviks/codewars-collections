"""https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa"""

from solution_categorize_new_member import open_or_senior


def test_fixed_tests__basic_test_cases():
    assert open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]) == ['Open', 'Senior', 'Open', 'Senior']
    assert open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]) == ['Open', 'Open', 'Senior', 'Open']
