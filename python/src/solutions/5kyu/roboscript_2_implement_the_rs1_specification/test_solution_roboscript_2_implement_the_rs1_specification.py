"""https://www.codewars.com/kata/5870fa11aa0428da750000da"""
import unittest

from solution_roboscript_2_implement_the_rs1_specification import execute


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(execute(""), "*")
        self.assertEqual(execute("FFFFF"), "******")
        self.assertEqual(execute("FFFFFLFFFFFLFFFFFLFFFFFL"),
                         "******\r\n*    *\r\n*    *\r\n*    *\r\n*    *\r\n******")
        self.assertEqual(execute("LFFFFFRFFFRFFFRFFFFFFF"),
                         "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   ")
        self.assertEqual(execute("LF5RF3RF3RF7"),
                         "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   ")
