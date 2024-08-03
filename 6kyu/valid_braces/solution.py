"""https://www.codewars.com/kata/5277c8a221e209d3f6000b56"""


def valid_braces(string):
    stack = []
    opening = '({['
    closing = ')}]'
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening.index(stack.pop()) != closing.index(char):
                return False
    return len(stack) == 0


def valid_braces_top_solution(string):
    while '{}' in string or '()' in string or '[]' in string:
        string = string.replace('{}', '')
        string = string.replace('[]', '')
        string = string.replace('()', '')
    return not string
