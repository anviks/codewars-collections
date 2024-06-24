"""https://www.codewars.com/kata/simpler-interactive-interpreter"""

import re


def tokenize(expression):
    if expression == '':
        return []

    regex = re.compile(r'\s*(=>|[-+*/%=()]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*')
    tokens = regex.findall(expression)
    
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        tokens = tokenize(expression)
        print(tokens)


def main():
    def pretty_compare(actual, expected):
        if actual != expected:
            print('\x1B[0;31m', end='')
            sign = '!='
        else:
            print('\x1B[0;32m', end='')
            sign = '=='
        print(repr(actual), sign, repr(expected), '\x1B[0m')
        
    interpreter = Interpreter()

    # Basic arithmetic
    pretty_compare(interpreter.input("1 + 1"), 2)
    pretty_compare(interpreter.input("2 - 1"), 1)
    pretty_compare(interpreter.input("2 * 3"), 6)
    pretty_compare(interpreter.input("8 / 4"), 2)
    pretty_compare(interpreter.input("7 % 4"), 3)

    # Variables
    pretty_compare(interpreter.input("x = 1"), 1)
    pretty_compare(interpreter.input("x"), 1)
    pretty_compare(interpreter.input("x + 3"), 4)
    # pretty_compare("input: 'y'", lambda: interpreter.input("y"))


if __name__ == '__main__':
    main()
