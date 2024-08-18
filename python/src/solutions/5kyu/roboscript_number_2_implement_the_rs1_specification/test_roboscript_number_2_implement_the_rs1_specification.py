"""https://www.codewars.com/kata/5870fa11aa0428da750000da"""

from solution_roboscript_number_2_implement_the_rs1_specification import *


def test_your_rs1_interpreter__should_work_for_the_example_tests_provided_in_the_description():
    assert execute('') == '*'
    assert execute('FFFFF') == '******'
    assert execute('FFFFFLFFFFFLFFFFFLFFFFFL') == '******\r\n*    *\r\n*    *\r\n*    *\r\n*    *\r\n******'
    assert execute('LFFFFFRFFFRFFFRFFFFFFF') == '    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   '
    assert execute('LF5RF3RF3RF7') == '    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   '
