"""https://www.codewars.com/kata/525f47c79f2f25a4db000025"""

import re


def valid_phone_number(phone_number: str):
    return bool(re.search(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number))
