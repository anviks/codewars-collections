"""https://www.codewars.com/kata/4-by-4-skyscrapers"""

from itertools import permutations


def get_clues(sequence: list[int]) -> list[int]:
    clues = [0, 0]
    largest = 0

    for i, seq in enumerate((sequence, sequence[::-1])):
        for square in seq:
            if square > largest:
                clues[i] += 1
                largest = square

        largest = 0

    return clues


def foo(clue1: int, sequence: list[int], clue2: int):
    perms = permutations({1, 2, 3, 4} - set(sequence), sequence.count(0))
    possibilities = []

    for perm in perms:
        new_sequence = list(sequence)

        for i, num in enumerate(new_sequence):
            if num == 0:
                new_sequence[i], *perm = perm

        if get_clues(new_sequence) == [clue1, clue2]:
            possibilities.append(new_sequence)

    if len(possibilities) == 1:
        return possibilities[0]
    else:
        return None


def solve_puzzle(clues):
    output = [[0] * 4] * 4

    while any(any(square == 0 for square in row) for row in output):
        for i, row in enumerate(output):
            new_row = foo(clues[15 - i], row, clues[4 + i])
            if new_row:
                output[i] = new_row

        output = list(zip(*output))

        for j, col in enumerate(output):
            new_col = foo(clues[j], col, clues[11 - j])
            if new_col:
                output[j] = new_col

        output = list(zip(*output))

    return tuple(output)
