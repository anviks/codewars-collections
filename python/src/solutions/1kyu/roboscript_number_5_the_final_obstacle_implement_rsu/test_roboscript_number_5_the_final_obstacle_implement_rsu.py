"""https://www.codewars.com/kata/5a12755832b8b956a9000133"""

import pytest

from solution_roboscript_number_5_the_final_obstacle_implement_rsu import RSUProgram
from tests_data import *


@pytest.mark.parametrize(
    "program, exp, msg",
    TESTS_THE_TOKENIZER1 + TESTS_THE_TOKENIZER2 + TESTS_THE_TOKENIZER3 + NEW_TESTS_TOKENIZER
)
def test_the_tokenizer(program, exp, msg):
    if exp:
        assert RSUProgram(program).get_tokens() == exp
    else:
        with pytest.raises(Exception):
            RSUProgram(program).get_tokens()


@pytest.mark.parametrize(
    "program, exp, msg",
    TESTS_THE_COMPILER_1 + TESTS_THE_COMPILER_2 + NEW_TESTS_COMPILER
)
def test_the_compiler(program, exp, msg):
    r = RSUProgram(program)
    if exp is not None:
        assert r.convert_to_raw(r.get_tokens()) == exp
    else:
        with pytest.raises(Exception):
            r.convert_to_raw(r.get_tokens())


@pytest.mark.parametrize(
    "program, exp, msg",
    TESTS_THE_MACHINE_1
)
def test_the_machine_instructions_executor(program, exp, msg):
    r = RSUProgram(program)
    if exp:
        assert r.execute_raw(r.convert_to_raw(r.get_tokens())) == exp
    else:
        raise Exception("Error tests routine not implemented")


@pytest.mark.parametrize(
    "program, exp, msg",
    TESTS_EXECUTE_1
)
def test_the_machine_instructions_executor(program, exp, msg):
    if exp:
        assert RSUProgram(program).execute() == exp
    else:
        raise Exception("Error tests routine not implemented")
