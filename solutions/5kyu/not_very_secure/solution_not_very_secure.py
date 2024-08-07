"""https://www.codewars.com/kata/526dbd6c8c0eb53254000110"""

import re


def alphanumeric(password):
    return bool(re.match(r'^\w+$', password)) and '_' not in password
