"""https://www.codewars.com/kata/55d5434f269c0c3f1b000058"""

import re


def triple_double(num1, num2):
    return bool(re.search(r'(\d)\1{2}\d*,\d*\1{2}', f'{num1},{num2}'))
