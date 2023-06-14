"""
https://www.codewars.com/kata/5277c8a221e209d3f6000b56

**Valid Braces**

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?\n
A string of braces is considered valid if all braces are matched with the correct brace.

Examples:
    "(){}[]"   =>  True\n
    "([{}])"   =>  True\n
    "(}"       =>  False\n
    "[(])"     =>  False\n
    "[({})](]" =>  False\n
"""


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


if __name__ == '__main__':
    print(valid_braces("(){}[]"))  # True
    print(valid_braces("([{}])"))  # True
    print(valid_braces("(}"))  # False
    print(valid_braces("[(])"))  # False
    print(valid_braces("[({})](]"))  # False
    print(valid_braces("(((({{"))  # False
