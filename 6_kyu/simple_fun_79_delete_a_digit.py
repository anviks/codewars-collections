"""https://www.codewars.com/kata/5894318275f2c75695000146"""


def delete_digit(n: int) -> int:
    str_n = str(n)
    return max(int(str_n[:i] + str_n[i + 1:]) for i in range(len(str_n)))


def main():
    from util_funcs import pretty_compare

    pretty_compare(delete_digit(152), 52)
    pretty_compare(delete_digit(1001), 101)
    pretty_compare(delete_digit(10), 1)


if __name__ == '__main__':
    main()
