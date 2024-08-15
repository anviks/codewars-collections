"""https://www.codewars.com/kata/594b898169c1d644f900002e"""
import unittest

from parameterized import parameterized

from solution_594b898169c1d644f900002e import execute


class YourRS3Interpreter(unittest.TestCase):
    @parameterized.expand([
        ('should work for RS2-compliant programs', [
            ('(F2LF2R)2FRF4L(F2LF2R)2(FRFL)4(F2LF2R)2', "    **   **      *\r\n    **   ***     *\r\n  **** *** **  ***\r\n  *  * *    ** *  \r\n***  ***     ***  ")
        ]),
        ('should properly parse a pattern definition and not cause any side effects', [
            ('p0(F2LF2R)2q', '*'),
            ('p312(F2LF2R)2q', '*')
        ]),
        ('should execute a given pattern when it is invoked', [
            ('p0(F2LF2R)2qP0', "    *\r\n    *\r\n  ***\r\n  *  \r\n***  "),
            ('p312(F2LF2R)2qP312', "    *\r\n    *\r\n  ***\r\n  *  \r\n***  ")
        ]),
        ('should always parse pattern definitions first before attempting to invoke them', [
            ('P0p0(F2LF2R)2q', "    *\r\n    *\r\n  ***\r\n  *  \r\n***  "),
            ('P312p312(F2LF2R)2q', "    *\r\n    *\r\n  ***\r\n  *  \r\n***  ")
        ]),
        ('should allow other forms of RoboScript code alongside pattern definitions and invocations', [
            ('F3P0Lp0(F2LF2R)2qF2', "       *\r\n       *\r\n       *\r\n       *\r\n     ***\r\n     *  \r\n******  ")
        ]),
        ('should allow a pattern to be invoked multiple times', [
            ('(P0)2p0F2LF2RqP0', "      *\r\n      *\r\n    ***\r\n    *  \r\n  ***  \r\n  *    \r\n***    ")
        ]),
        ('should properly parse multiple pattern definitions', [
            ('P1P2p1F2Lqp2F2RqP2P1', "  ***\r\n  * *\r\n*** *"),
            ('p1F2Lqp2F2Rqp3P1(P2)2P1q(P3)3', "  *** *** ***\r\n  * * * * * *\r\n*** *** *** *")
        ]),
    ])
    def test_should_pass(self, msg, test_cases):
        for code, expected in test_cases:
            self.assertEqual(expected, execute(code), msg)
        
    @parameterized.expand([
        ('should throw an error when a non-existing pattern is invoked', [
            ('Your interpreter should throw an error because pattern "P1" does not exist', 'p0(F2LF2R)2qP1'),
            ('Your interpreter should throw an error because pattern "P0" does not exist', 'P0p312(F2LF2R)2q'),
            ('Your interpreter should throw an error because pattern "P312" does not exist', 'P312')
        ]),
        ('should throw an error when a pattern is defined more than once', [
            ('Your interpreter should throw an error since pattern "P1" is defined twice', 'p1F2Lqp1(F3LF4R)5qp2F2Rqp3P1(P2)2P1q(P3)3')
        ]),
        ('should throw an error when any form of infinite recursion is detected', [
            ('should throw an error when any form of infinite recursion is detected', 'p1F2RP1F2LqP1'),
            ('Your interpreter should throw an error since pattern "P1" invokes "P2" which then again invokes "P1", creating an infinite cycle', 'p1F2LP2qp2F2RP1qP1')
        ])
    ])
    def test_should_fail(self, _, test_cases):
        for why, code in test_cases:
            with self.assertRaises(Exception) as context:
                execute(code)
