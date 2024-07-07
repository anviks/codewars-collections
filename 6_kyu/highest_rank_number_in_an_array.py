"""https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004"""


def highest_rank(arr):
    return max(set(arr), key=lambda x: (arr.count(x), x))


def main():
    from util_funcs import pretty_compare

    pretty_compare(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
    pretty_compare(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
    pretty_compare(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12)
    pretty_compare(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]), 3)
    pretty_compare(highest_rank([1, 2, 3]), 3)
    pretty_compare(highest_rank([1, 1, 2, 3]), 1)
    pretty_compare(highest_rank([1, 1, 2, 2, 3]), 2)


if __name__ == '__main__':
    main()
