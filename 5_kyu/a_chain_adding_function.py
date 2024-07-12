"""https://www.codewars.com/kata/539a0e4d85e3425cb0000a88"""


class add(int):
    def __call__(self, n):
        return add(self + n)


def main():
    from util_funcs import pretty_compare

    pretty_compare(add(1), 1)
    pretty_compare(add(1)(2), 3)
    pretty_compare(add(1)(2)(3), 6)


if __name__ == '__main__':
    main()
