"""https://www.codewars.com/kata/58738d518ec3b4bf95000192"""
import unittest

from solution_58738d518ec3b4bf95000192 import execute


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(execute("LF5(RF3)(RF3R)F7"),
                         "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   ")
        self.assertEqual(execute("(L(F5(RF3))(((R(F3R)F7))))"),
                         "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   ")
        self.assertEqual(execute("F4L(F4RF4RF4LF4L)2F4RF4RF4"),
                         "    *****   *****   *****\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n*****   *****   *****   *")
        self.assertEqual(execute("F4L((F4R)2(F4L)2)2(F4R)2F4"),
                         "    *****   *****   *****\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n    *   *   *   *   *   *\r\n*****   *****   *****   *")
