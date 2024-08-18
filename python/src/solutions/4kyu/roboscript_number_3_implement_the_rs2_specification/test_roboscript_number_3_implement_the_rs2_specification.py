"""https://www.codewars.com/kata/58738d518ec3b4bf95000192"""

from solution_roboscript_number_3_implement_the_rs2_specification import *


def test_your_rs2_interpreter__should_work_for_the_example_tests_provided_in_the_description():
    assert execute('LF5(RF3)(RF3R)F7') == '    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   '
    assert execute(
        '(L(F5(RF3))(((R(F3R)F7))))') == '    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   '
    assert execute(
        'F4L(F4RF4RF4LF4L)2F4RF4RF4') == '    *****   *****   *****\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n*****   *****   *****   *'
    assert execute(
        'F4L((F4R)2(F4L)2)2(F4R)2F4') == '    *****   *****   *****\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n*****   *****   *****   *'
