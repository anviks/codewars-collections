"""https://www.codewars.com/kata/simpler-interactive-interpreter"""

import pytest

from solution_simpler_interactive_interpreter import Interpreter

interpreter = Interpreter()


def test_arithmetic():
    assert interpreter.input('1 + 1') == 2
    assert interpreter.input('2 - 1') == 1
    assert interpreter.input('2 * 3') == 6
    assert interpreter.input('8 / 4') == 2
    assert interpreter.input('7 % 4') == 3


def test_variable():
    assert interpreter.input('x = 1') == 1
    assert interpreter.input('x') == 1
    assert interpreter.input('x + 3') == 4
    with pytest.raises(Exception):
        interpreter.input('y')
