"""https://www.codewars.com/kata/54a91a4883a7de5d7800009c"""
import re


def increment_string(strng):
    m = re.search(r'^(.*?)(\d*)$', strng)
    p1, p2 = m.groups()
    return p1 + str(int(p2 or 0) + 1).zfill(len(p2))


def main():
    print(increment_string("foo"), "foo1")
    print(increment_string("foobar001"), "foobar002")
    print(increment_string("foobar1"), "foobar2")
    print(increment_string("foobar00"), "foobar01")
    print(increment_string("foobar99"), "foobar100")
    print(increment_string("foobar099"), "foobar100")
    print(increment_string("fo99obar99"), "fo99obar100")
    print(increment_string(""), "1")


if __name__ == '__main__':
    main()
