"""https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9"""


def up_array(arr: list[int]) -> list[int] | None:
    if any(n < 0 or n > 9 for n in arr):
        return None
    
    num = int(''.join(str(d) for d in arr)) + 1
    
    return [int(d) for d in str(num).zfill(len(arr))]


def main():
    from util_funcs import pretty_compare

    pretty_compare(up_array([2, 3, 9]), [2, 4, 0])
    pretty_compare(up_array([9, 9]), [1, 0, 0])
    pretty_compare(up_array([0, 4, 2]), [0, 4, 3])
    pretty_compare(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
    pretty_compare(up_array([1, 2, 3, 9]), [1, 2, 4, 0])
    pretty_compare(up_array([9, 9, 9, 9]), [1, 0, 0, 0, 0])
    pretty_compare(up_array([0, 1, 3, 7]), [0, 1, 3, 8])
    pretty_compare(up_array([1, -9]), None)


if __name__ == '__main__':
    main()
