"""https://www.codewars.com/kata/56a921fa8c5167d8e7000053"""

import re


def password(string):
    return bool(re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}", string))
