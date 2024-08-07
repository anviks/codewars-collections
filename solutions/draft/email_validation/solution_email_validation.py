"""https://www.codewars.com/kata/53855e4dc25c8adbc5000316"""

import re


def validate(email: str) -> bool:
    return bool(re.search(r"^[a-z]\w*@[\w-]+(\.\w+)+$", email))
