"""https://www.codewars.com/kata/56fb3cde26cc99c2fd000009"""
from string import ascii_lowercase
from codecs import encode


def encrypter(s):
    rot13 = encode(s, 'rot13')
    return ''.join(ascii_lowercase[-ascii_lowercase.index(char) - 1] if char in ascii_lowercase else char for char in rot13)
