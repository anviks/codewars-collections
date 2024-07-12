"""https://www.codewars.com/kata/55d5434f269c0c3f1b000058"""
import re


def triple_double(num1, num2):
    return bool(re.search(r'(\d)\1{2}\d*,\d*\1{2}', f'{num1},{num2}'))


def main():
    from util_funcs import pretty_compare

    pretty_compare(triple_double(451999277, 41177722899), 1)
    pretty_compare(triple_double(1222345, 12345), 0)
    pretty_compare(triple_double(12345, 12345), 0)
    pretty_compare(triple_double(666789, 12345667), 1)
    pretty_compare(triple_double(10560002, 100), 1)
    pretty_compare(triple_double(1112, 122), 0)


if __name__ == '__main__':
    main()
