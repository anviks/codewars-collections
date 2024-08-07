"""https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991"""


def rev_rot(strng: str, sz: int):
    if sz <= 0 or strng == '':
        return ''
    new_string = ''

    for i in range(0, len(strng) - len(strng) % sz, sz):
        nums = [int(d) for d in strng[i:i + sz]]

        if sum(nums) % 2 == 0:
            nums = nums[::-1]
        else:
            nums.append(nums.pop(0))

        new_string += ''.join(map(str, nums))

    return new_string
