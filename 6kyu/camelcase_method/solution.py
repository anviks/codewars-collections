"""https://www.codewars.com/kata/587731fda577b3d1b0001196"""

import re


def camel_case(s: str):
    return re.sub(r'(?:^| )([a-z])', lambda m: m.group(1).upper(), s).strip()
