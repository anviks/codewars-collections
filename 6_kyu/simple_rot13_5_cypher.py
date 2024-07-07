"""https://www.codewars.com/kata/5894986e2ddc8f6805000036"""
import re
from codecs import encode


def rot_135(st):
    return re.sub(r'\d', lambda m: str((int(m.group()) + 5) % 10), encode(st, 'rot13'))


def main():
    from util_funcs import pretty_compare

    pretty_compare(rot_135("The quick brown fox jumps over the 2 lazy dogs"),
                   "Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf")
    pretty_compare(rot_135("Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf"),
                   "The quick brown fox jumps over the 2 lazy dogs")


if __name__ == '__main__':
    main()
