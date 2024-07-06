"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b"""


def parts_sums(nums: list[int]) -> list[int]:
    current_sum = sum(nums)
    sums = [current_sum]
    
    for n in nums:
        current_sum -= n
        sums.append(current_sum)
    
    return sums


def main():
    print(parts_sums([]), [0], sep='\n', end='\n\n')
    print(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0], sep='\n', end='\n\n')
    print(parts_sums([1, 2, 3, 4, 5, 6]), [21, 20, 18, 15, 11, 6, 0], sep='\n', end='\n\n')


if __name__ == '__main__':
    main()



