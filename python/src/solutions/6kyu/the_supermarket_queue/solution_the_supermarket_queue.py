"""https://www.codewars.com/kata/57b06f90e298a7b53d000a86"""


def queue_time(customers: list[int], n: int):
    result = 0

    while customers:
        customers[:n] = [m - 1 for m in customers[:n] if m - 1 > 0]
        result += 1

    return result
