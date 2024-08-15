"""
https://www.codewars.com/kata/5a331ea7ee1aae8f24000175

Total tests execution time: 4110ms
Random tests execution time: 3582ms
"""


def triangle(row: str):
    chunk_sizes = (3 ** i + 1 for i in range(9, -1, -1))
    mapper = {'R': 0, 0: 'R', 'G': 1, 1: 'G', 'B': 2, 2: 'B'}
    row = [mapper[char] for char in row]
    len_row = len(row)

    for size in chunk_sizes:
        while len_row >= size:
            # Instead of creating a new list every time, modify the original and pretend it's shorter
            len_row = len_row - size + 1
            for i in range(len_row):
                # If they're the same, don't modify row[i]
                if row[i] != row[i + size - 1]:
                    row[i] = 3 - row[i] - row[i + size - 1]

    return mapper[row[0]]
