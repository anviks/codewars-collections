"""https://www.codewars.com/kata/59c633e7dcc4053512000073"""
import re


def solve(s: str):
    return max(
        sum(ord(c) - 96 for c in m)
        for m in re.findall(r'[b-df-hj-np-tv-z]+', s)
    )


def main():
    from util_funcs import pretty_compare
    pretty_compare(solve("cozy"), 51)
    pretty_compare(solve("xyzzy"), 126)
    pretty_compare(solve("zodiac"), 26)
    pretty_compare(solve("chruschtschov"), 80)
    pretty_compare(solve("khrushchev"), 38)
    pretty_compare(solve("strength"), 57)
    pretty_compare(solve("catchphrase"), 73)
    pretty_compare(solve("twelfthstreet"), 103)
    pretty_compare(solve("mischtschenkoana"), 80)


if __name__ == '__main__':
    main()
