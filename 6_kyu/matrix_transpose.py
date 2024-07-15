"""https://www.codewars.com/kata/52fba2a9adcd10b34300094c"""


def transpose(matrix):
    return [list(t) for t in zip(*matrix)]


def main():
    from util_funcs import pretty_compare

    pretty_compare(transpose([[1]]), [[1]])
    pretty_compare(transpose([[1, 2, 3]]), [[1], [2], [3]])
    pretty_compare(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    pretty_compare(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]),
                   [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])


if __name__ == '__main__':
    main()
