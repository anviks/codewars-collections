"""https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c"""


def max_sequence(arr):
    if not arr:
        return 0

    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
        else:
            max_current += arr[i]

        if max_current > max_global:
            max_global = max_current

    return max(max_global, 0)
