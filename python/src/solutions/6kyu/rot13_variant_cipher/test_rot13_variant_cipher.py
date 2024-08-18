"""https://www.codewars.com/kata/56fb3cde26cc99c2fd000009"""

from solution_rot13_variant_cipher import *


def test_basic_tests():
    assert encrypter('amz') == 'man'
    assert encrypter('welcome to the organization') == 'qibkyai ty tfi yvgmzenmteyz', \
        "Expect 'welcome to our organization' to return 'qibkyai ty ysv yvgmzenmteyz'"
    assert encrypter('hello') == 'fibby', "Expect 'hello' to return 'fibby'"
    assert encrypter('my name is') == 'ao zmai eu', "Expect 'my name is' to return 'ao zmai eu'"
    assert encrypter('goodbye') == 'gyyjloi', "Expect 'goodbye' to return 'gyyjloi'"
