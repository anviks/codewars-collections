"""https://www.codewars.com/kata/660d55d0ba01e5016c85cfeb"""

import functools as f
slice=lambda a,b:f.reduce(lambda c,d:c+d,map(chr,range(ord(a),ord(b)+1)))


def main():
    from util_funcs import pretty_compare

    pretty_compare(slice("A", "A"), "A")
    pretty_compare(slice("A", "F"), "ABCDEF")

    pretty_compare(slice("l", "l"), "l")
    pretty_compare(slice("a", "z"), "abcdefghijklmnopqrstuvwxyz")


if __name__ == '__main__':
    main()
