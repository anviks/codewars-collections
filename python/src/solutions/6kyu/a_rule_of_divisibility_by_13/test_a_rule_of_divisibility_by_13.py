"""https://www.codewars.com/kata/564057bc348c7200bd0000ff"""

from solution_a_rule_of_divisibility_by_13 import *


def test_thirt__fixed_tests():
    assert thirt(8529) == 79
    assert thirt(85299258) == 31
    assert thirt(5634) == 57
    assert thirt(1111111111) == 71
    assert thirt(987654321) == 30
