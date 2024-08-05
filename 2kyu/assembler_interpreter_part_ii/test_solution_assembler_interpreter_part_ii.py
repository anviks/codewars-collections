"""https://www.codewars.com/kata/assembler-interpreter-part-ii"""

import unittest

from parameterized import parameterized

from solution_assembler_interpreter_part_ii import assembler_interpreter


class SampleTests(unittest.TestCase):
    @parameterized.expand([
        ['assembler_code_snippets/simple_program', '(5+1)/2 = 3'],
        ['assembler_code_snippets/factorial', '5! = 120'],
        ['assembler_code_snippets/fibonacci', 'Term 8 of Fibonacci series is: 21'],
        ['assembler_code_snippets/modulo', 'mod(11, 3) = 2'],
        ['assembler_code_snippets/gcd', 'gcd(81, 153) = 9'],
        ['assembler_code_snippets/failing', -1],
        ['assembler_code_snippets/power', '2^10 = 1024'],
    ])
    def test_examples(self, file_path, expected_output):
        with open(file_path) as f:
            self.assertEqual(expected_output, assembler_interpreter(f.read()))
