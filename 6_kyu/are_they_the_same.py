"""https://www.codewars.com/kata/550498447451fbbd7600041c"""


def comp(array1, array2):
    return sorted(map(lambda x: x ** 2, array1)) == sorted(array2) if array1 and array2 else array1 == array2 == []


def main():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    print(comp(a1, a2))


if __name__ == '__main__':
    main()
