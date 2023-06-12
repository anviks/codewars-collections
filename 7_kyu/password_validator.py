"""
Description
Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

There needs to be at least 1 uppercase letter.
There needs to be at least 1 lowercase letter.
There needs to be at least 1 number.
The password needs to be at least 8 characters long.
You are permitted to use any methods to validate the password.
"""

import re


def password(string):
    return bool(re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}", string))


if __name__ == '__main__':
    assert password("Abcd1234")
    assert not password("Abcd123")
    assert not password("abcd1234")
    assert password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890")
    assert not password("ABCD1234")
    assert password(r"Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,")
    assert not password(r"!@#$%^&*()-_+={}[]|\:;?/>.<,")
    assert not password("")
    assert password(" aA1----")
    assert password("4aA1----")
