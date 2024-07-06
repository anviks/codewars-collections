"""https://www.codewars.com/kata/559a28007caad2ac4e000083"""


def perimeter(n):
    acc = 1
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b
        acc += b

    return 4 * acc


def main():
    print(perimeter(5))  # 80
    print(perimeter(7))  # 216


if __name__ == '__main__':
    main()
