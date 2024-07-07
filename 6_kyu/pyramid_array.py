"""https://www.codewars.com/kata/515f51d438015969f7000013"""


def pyramid(n):
    return [[1] * i for i in range(1, n + 1)]


def main():
    from util_funcs import pretty_compare

    pretty_compare(pyramid(0), [])
    pretty_compare(pyramid(1), [[1]])
    pretty_compare(pyramid(2), [[1], [1, 1]])
    pretty_compare(pyramid(3), [[1], [1, 1], [1, 1, 1]])


if __name__ == '__main__':
    main()
