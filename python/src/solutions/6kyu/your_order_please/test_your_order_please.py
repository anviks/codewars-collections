"""https://www.codewars.com/kata/55c45be3b2079eccff00010f"""

from solution_your_order_please import *


def test_your_order_please__sample_tests():
    assert order('is2 Thi1s T4est 3a') == 'Thi1s is2 3a T4est'
    assert order('4of Fo1r pe6ople g3ood th5e the2') == 'Fo1r the2 g3ood 4of th5e pe6ople'
    assert order('') == ''
