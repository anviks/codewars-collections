"""https://www.codewars.com/kata/simple-assembler-interpreter"""


import unittest
from solution_58e24788e24ddee28e000053 import simple_assembler

class SampleTests(unittest.TestCase):
    def test_tests(self):
        code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
        self.assertEqual(simple_assembler(code.splitlines()), {'a': 1})

        code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
        self.assertEqual(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})
