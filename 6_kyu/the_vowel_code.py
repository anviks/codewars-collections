"""https://www.codewars.com/kata/53697be005f803751e0015aa"""
import re


def encode(st: str):
    return re.sub(r'[aeiou]', lambda m: str('aeiou'.index(m.group()) + 1), st)


def decode(st: str):
    return re.sub(r'[1-5]', lambda m: 'aeiou'[int(m.group()) - 1], st)


def main():
    from util_funcs import pretty_compare

    pretty_compare(encode('hello'), 'h2ll4')
    pretty_compare(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
    pretty_compare(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
    pretty_compare(decode('h2ll4'), 'hello')


if __name__ == '__main__':
    main()
