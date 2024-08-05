"""https://www.codewars.com/kata/526156943dfe7ce06200063e"""
import unittest

from solution_my_smallest_code_interpreter_aka_brainf_k import brain_luck


# Echo until byte(255) encountered
class SolutionTests(unittest.TestCase):
    def test_echo_until_byte_255_encountered(self):
        self.assertEqual(brain_luck(',+[-.,+]', 'Codewars' + chr(255)), 'Codewars')

    def test_echo_until_byte_0_encountered(self):
        self.assertEqual(brain_luck(',[.[-],]', 'Codewars' + chr(0)), 'Codewars')

    def test_two_numbers_multiplier(self):
        self.assertEqual(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), chr(72))
