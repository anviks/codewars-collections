"""https://www.codewars.com/kata/59df2f8f08c6cec835000012"""


def meeting(s: str):
    people = []

    for name in s.upper().split(';'):
        first, last = name.split(':')
        people.append((last, first))

    return ''.join(f'({last}, {first})' for last, first in sorted(people))
