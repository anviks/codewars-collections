"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b"""


def parts_sums(nums: list[int]) -> list[int]:
    current_sum = sum(nums)
    sums = [current_sum]

    for n in nums:
        current_sum -= n
        sums.append(current_sum)

    return sums
