"""https://www.codewars.com/kata/assembler-interpreter-part-ii"""
import os.path

import pytest

from solution_assembler_interpreter_part_ii import assembler_interpreter


@pytest.mark.parametrize('file_path, expected_output', [
    ('assembler_code_snippets/simple_program', '(5+1)/2 = 3'),
    ('assembler_code_snippets/factorial', '5! = 120'),
    ('assembler_code_snippets/fibonacci', 'Term 8 of Fibonacci series is: 21'),
    ('assembler_code_snippets/modulo', 'mod(11, 3) = 2'),
    ('assembler_code_snippets/gcd', 'gcd(81, 153) = 9'),
    ('assembler_code_snippets/failing', -1),
    ('assembler_code_snippets/power', '2^10 = 1024'),
])
def test_examples(file_path, expected_output):
    with open(os.path.join(os.path.dirname(__file__), file_path)) as f:
        assert assembler_interpreter(f.read()) == expected_output
