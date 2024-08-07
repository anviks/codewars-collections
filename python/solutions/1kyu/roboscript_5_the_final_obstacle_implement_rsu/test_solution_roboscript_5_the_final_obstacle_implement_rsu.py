"""https://www.codewars.com/kata/5a12755832b8b956a9000133"""
import unittest

from solution_roboscript_5_the_final_obstacle_implement_rsu import RSUProgram
from tests_data import *


class TheTokenizer(unittest.TestCase):
    def run_tests(self, config_tests):
        for program, exp, msg in config_tests:
            if exp:
                self.assertEqual(RSUProgram(program).get_tokens(), exp)
            else:
                self.assertRaises(Exception, RSUProgram(program).get_tokens)

    TEST_CONFIG = (
        ('should correctly tokenize valid RSU program', TESTS_THE_TOKENIZER1),
        ('should throw an error if one or more invalid tokens are detected', TESTS_THE_TOKENIZER2),
        ('should correctly tokenize invalid RSU programs containing only valid tokens', TESTS_THE_TOKENIZER3),
        ('Additional tests', NEW_TESTS_TOKENIZER),
    )

    def test_tokenizer(self):
        for msg, data in self.TEST_CONFIG:
            self.run_tests(data)


class TheCompiler(unittest.TestCase):
    def run_tests(self, config_tests):
        for program, exp, msg in config_tests:
            r = RSUProgram(program)
            if exp is not None:
                self.assertEqual(r.convert_to_raw(r.get_tokens()), exp)
            else:
                self.assertRaises(Exception, r.convert_to_raw, r.get_tokens())

    TEST_CONFIG = (
        ('should correctly convert valid RSU token sequences into raw command sequences', TESTS_THE_COMPILER_1),
        ('should throw an error with invalid RSU programs or valid programs with runtime errors', TESTS_THE_COMPILER_2),
        ('Additional tests', NEW_TESTS_COMPILER),
    )

    def test_compiler(self):
        for msg, data in self.TEST_CONFIG:
            self.run_tests(data)


class TheMachineInstructionsExecutor(unittest.TestCase):
    def run_tests(self, config_tests):
        for program, exp, msg in config_tests:
            r = RSUProgram(program)
            if exp:
                self.assertEqual(r.execute_raw(r.convert_to_raw(r.get_tokens())), exp)
            else:
                raise Exception("Error tests routine not implemented")

    TEST_CONFIG = (
        ('should work for the example provided in the Description', TESTS_THE_MACHINE_1),
    )

    def test_machine(self):
        for msg, data in self.TEST_CONFIG:
            self.run_tests(data)


class TheMachineInstructionExecutor(unittest.TestCase):
    def run_tests(self, config_tests):
        for program, exp, msg in config_tests:
            if exp:
                self.assertEqual(RSUProgram(program).execute(), exp)
            else:
                raise Exception("Error tests routine not implemented")

    TEST_CONFIG = (
        ('should work for the example provided in the Description', TESTS_EXECUTE_1),
    )

    def test_machine(self):
        for msg, data in self.TEST_CONFIG:
            self.run_tests(data)
