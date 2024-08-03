"""https://www.codewars.com/kata/56fb3cde26cc99c2fd000009"""

import unittest
from solution import encrypter


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(encrypter("amz"), "man", )
        self.assertEqual(encrypter("welcome to the organization"), "qibkyai ty tfi yvgmzenmteyz",
                         "Expect 'welcome to our organization' to return 'qibkyai ty ysv yvgmzenmteyz'")
        self.assertEqual(encrypter("hello"), "fibby", "Expect 'hello' to return 'fibby'")
        self.assertEqual(encrypter("my name is"), "ao zmai eu", "Expect 'my name is' to return 'ao zmai eu'")
        self.assertEqual(encrypter("goodbye"), "gyyjloi", "Expect 'goodbye' to return 'gyyjloi'")
