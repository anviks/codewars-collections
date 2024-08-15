"""https://www.codewars.com/kata/54dc6f5a224c26032800005c"""

import unittest

from solution_help_the_bookseller import stock_list


class Testing(unittest.TestCase):
    def test_tests(self):
        b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B", "C", "D"]
        self.assertEqual(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        self.assertEqual(stock_list(b, c), "(A : 200) - (B : 1140)")
