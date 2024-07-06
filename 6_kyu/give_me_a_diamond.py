"""https://www.codewars.com/kata/5503013e34137eeeaa001648"""


def diamond(n: int) -> str | None:
    if n % 2 == 0 or n < 0:
        return None

    rows: list[str] = [' ' * ((n - num) // 2) + '*' * num for num in range(1, n + 1, 2)]
    rows.extend(rows[-2::-1])

    return '\n'.join(rows) + '\n'


def main():
    print(diamond(1))
    print(diamond(2))
    print(diamond(3))
    print(diamond(5))
    print(diamond(0))


if __name__ == '__main__':
    main()
