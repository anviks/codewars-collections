"""https://www.codewars.com/kata/55c04b4cc56a697bb0000048"""

from collections import Counter


def scramble(s1: str, s2: str):
    c1, c2 = Counter(s1), Counter(s2)
    c2.subtract(c1)
    print(c2)
    print(c2 - c1)
    # c1.subtract(c2)
    # return c1.most_common()[-1][1] >= 0


def main():
    print(scramble('rkqodlw', 'world') is True)
    print(scramble('cedewaraaossoqqyt', 'codewars') is True)
    print(scramble('katas', 'steak') is False)


if __name__ == '__main__':
    main()
