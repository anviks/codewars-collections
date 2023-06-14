"""
https://www.codewars.com/kata/52efefcbcdf57161d4000091

**Count characters in your string**

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

import collections


def count(s: str):
    return collections.Counter(s)


def count2(s: str):
    return {c: s.count(c) for c in set(s)}


if __name__ == '__main__':
    print(count("aba"))  # {'a': 2, 'b': 1}
    print(count(""))  # {}
    print(count("a" * 1000000))  # {'a': 1000000}
    print(count2("aba"))  # {'a': 2, 'b': 1}
    print(count2(""))  # {}
    print(count2("a" * 1000000))  # {'a': 1000000}

    # Chad solution:
    # from collections import Counter as count
