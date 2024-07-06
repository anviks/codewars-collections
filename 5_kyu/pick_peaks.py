"""https://www.codewars.com/kata/5279f6fe5ab7f447890006a7"""


def old_pick_peaks(arr: list[int]) -> dict[str, list[int]]:
    result = {'pos': [], 'peaks': []}

    for i in range(1, len(arr) - 1):
        if arr[i - 1] == arr[i]:
            continue

        l, r = i - 1, i + 1

        broken = False

        while arr[l] == arr[i]:
            l -= 1
            if l < 0:
                broken = True
                break

        while arr[r] == arr[i]:
            r += 1
            if r == len(arr):
                broken = True
                break

        if broken:
            break

        if arr[l] < arr[i] > arr[r]:
            result['pos'].append(i)
            result['peaks'].append(arr[i])

    return result


def pick_peaks(arr: list[int]) -> dict[str, list[int]]:
    result = {'pos': [], 'peaks': []}
    real_positions = [0]
    i = 1
    shift = 0

    while i < len(arr):
        while i < len(arr) and arr[i] == arr[i - 1]:
            arr.pop(i)
            shift += 1
        real_positions.append(i + shift)
        i += 1

    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            result['pos'].append(real_positions[i])
            result['peaks'].append(arr[i])

    return result


def main():
    from util_funcs import pretty_compare
    pretty_compare(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})
    pretty_compare(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})
    pretty_compare(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {"pos": [3, 7, 10], "peaks": [6, 3, 2]})
    pretty_compare(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})
    pretty_compare(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})
    pretty_compare(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), {"pos": [2], "peaks": [3]})
    pretty_compare(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]), {"pos": [2], "peaks": [3]})
    pretty_compare(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]),
                   {"pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]})
    pretty_compare(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]),
                   {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
    pretty_compare(pick_peaks([]), {"pos": [], "peaks": []})
    pretty_compare(pick_peaks([1, 1, 1, 1]), {"pos": [], "peaks": []})
    pretty_compare(pick_peaks([14, -4, 1, -1, -5, 17, 19, -3, 4, 19, 16, 4, 4, 19, 18]), {'pos': [2, 6, 9, 13], 'peaks': [1, 19, 19, 19]})


if __name__ == '__main__':
    main()
