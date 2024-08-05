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
