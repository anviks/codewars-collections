"""https://www.codewars.com/kata/58235a167a8cb37e1a0000db"""
from collections import Counter


def number_of_pairs(gloves: list[str]):
    return sum(n // 2 for n in Counter(gloves).values())


def main():
    from util_funcs import pretty_compare

    pretty_compare(number_of_pairs(["red", "red"]), 1)
    pretty_compare(number_of_pairs(["red", "green", "blue"]), 0)
    pretty_compare(number_of_pairs(["gray", "black", "purple", "purple", "gray", "black"]), 3)
    pretty_compare(number_of_pairs([]), 0)
    pretty_compare(number_of_pairs(["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]), 4)


if __name__ == '__main__':
    main()
