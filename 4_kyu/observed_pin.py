"""https://www.codewars.com/kata/5263c6999e0f40dee200059d"""

from itertools import product


def get_pins(observed: str) -> list[str]:
    possibilities: list[list[str]] = []

    for digit in observed:
        num = int(digit) or 11
        digit_possibilities = [digit]

        for neighbour in [num - 3, num - 1, num + 1, num + 3]:
            if neighbour <= 0:
                continue
            if neighbour == 11:
                neighbour = 0
            if neighbour >= 10:
                continue
            # This condition eliminates 'false' neighbours like 6 and 7
            if (neighbour % 3) ^ (num % 3) == 1:
                continue

            digit_possibilities.append(str(neighbour))

        possibilities.append(digit_possibilities)

    return [''.join(p) for p in product(*possibilities)]


def main():
    print(sorted(get_pins('8')))  # ['0', '5', '7', '8', '9']
    print(sorted(get_pins('0')))  # ['0', '8']
    print(sorted(get_pins('11')))  # ['11', '12', '14', '21', '22', '24', '41', '42', '44']
    print(sorted(get_pins('369')))
    # [
    #     '236', '238', '239', '256', '258', '259', '266', '268', '269',
    #     '296', '298', '299', '336', '338', '339', '356', '358', '359',
    #     '366', '368', '369', '396', '398', '399', '636', '638', '639',
    #     '656', '658', '659', '666', '668', '669', '696', '698', '699'
    # ]
# ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']
# ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']


if __name__ == '__main__':
    main()
