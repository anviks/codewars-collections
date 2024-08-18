"""https://www.codewars.com/kata/594b898169c1d644f900002e"""

import pytest

from solution_roboscript_number_4_rs3_patterns_to_the_rescue import *


def test_your_rs3_interpreter():

    def assert_path_equals(actual, expected):
        if actual != expected:
            print('You returned:')
            print(actual)
            print('Expected path of MyRobot:')
            print(expected)
        assert actual == expected

    def expect_error(why, code):
        with pytest.raises(Exception):
            execute(code)

    tests = [('should work for RS2-compliant programs', [
        lambda: assert_path_equals(execute('(F2LF2R)2FRF4L(F2LF2R)2(FRFL)4(F2LF2R)2'),
                                   '    **   **      *\r\n    **   ***     *\r\n  **** *** **  ***\r\n  *  * *    ** *  \r\n***  ***     ***  ')]),
             ('should properly parse a pattern definition and not cause any side effects',
              [lambda: assert_path_equals(execute('p0(F2LF2R)2q'), '*'),
               lambda: assert_path_equals(execute('p312(F2LF2R)2q'), '*')]), (
             'should execute a given pattern when it is invoked',
             [lambda: assert_path_equals(execute('p0(F2LF2R)2qP0'), '    *\r\n    *\r\n  ***\r\n  *  \r\n***  '),
              lambda: assert_path_equals(execute('p312(F2LF2R)2qP312'), '    *\r\n    *\r\n  ***\r\n  *  \r\n***  ')]),
             ('should always parse pattern definitions first before attempting to invoke them',
              [lambda: assert_path_equals(execute('P0p0(F2LF2R)2q'), '    *\r\n    *\r\n  ***\r\n  *  \r\n***  '),
               lambda: assert_path_equals(execute('P312p312(F2LF2R)2q'), '    *\r\n    *\r\n  ***\r\n  *  \r\n***  ')]),
             ('should allow other forms of RoboScript code alongside pattern definitions and invocations', [
                 lambda: assert_path_equals(execute('F3P0Lp0(F2LF2R)2qF2'),
                                            '       *\r\n       *\r\n       *\r\n       *\r\n     ***\r\n     *  \r\n******  ')]),
             ('should allow a pattern to be invoked multiple times', [
                 lambda: assert_path_equals(execute('(P0)2p0F2LF2RqP0'),
                                            '      *\r\n      *\r\n    ***\r\n    *  \r\n  ***  \r\n  *    \r\n***    ')]),
             ('should throw an error when a non-existing pattern is invoked', [
                 lambda: expect_error('Your interpreter should throw an error because pattern "P1" does not exist',
                                      'p0(F2LF2R)2qP1'),
                 lambda: expect_error('Your interpreter should throw an error because pattern "P0" does not exist',
                                      'P0p312(F2LF2R)2q'),
                 lambda: expect_error('Your interpreter should throw an error because pattern "P312" does not exist',
                                      'P312')]), ('should properly parse multiple pattern definitions', [
            lambda: assert_path_equals(execute('P1P2p1F2Lqp2F2RqP2P1'), '  ***\r\n  * *\r\n*** *'),
            lambda: assert_path_equals(execute('p1F2Lqp2F2Rqp3P1(P2)2P1q(P3)3'),
                                       '  *** *** ***\r\n  * * * * * *\r\n*** *** *** *')]), (
             'should throw an error when a pattern is defined more than once', [
                 lambda: expect_error('Your interpreter should throw an error since pattern "P1" is defined twice',
                                      'p1F2Lqp1(F3LF4R)5qp2F2Rqp3P1(P2)2P1q(P3)3')]), (
             'should throw an error when any form of infinite recursion is detected', [
                 lambda: expect_error('should throw an error when any form of infinite recursion is detected',
                                      'p1F2RP1F2LqP1'), lambda: expect_error(
                     'Your interpreter should throw an error since pattern "P1" invokes "P2" which then again invokes "P1", creating an infinite cycle',
                     'p1F2LP2qp2F2RP1qP1')])]
    
    for scenario in tests:
        message, assertions = scenario
        
        for assertion in assertions:
            assertion()
