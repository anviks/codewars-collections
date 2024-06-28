"""https://www.codewars.com/kata/5592e3bd57b64d00f3000047"""


def find_nb(m):
    for i in range(1, m):
        m -= i ** 3
        
        if m == 0:
            return i
        elif m < 0:
            return -1


def main():
    print(find_nb(4), -1)
    print(find_nb(16), -1)
    print(find_nb(4183059834009), 2022)


if __name__ == '__main__':
    main()

