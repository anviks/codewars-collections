"""https://www.codewars.com/kata/one-line-task-zero-or-one"""


zero_or_one=lambda n,s:[sum(c)>n/2 for c in zip(*s)]


def main():
    actual = zero_or_one(5, [[1, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 1, 0],
                             [0, 0, 0, 0, 1]])
    expected = [0, 0, 0, 0, 0]
    print(actual)
    print(actual == expected)


if __name__ == '__main__':
    main()
