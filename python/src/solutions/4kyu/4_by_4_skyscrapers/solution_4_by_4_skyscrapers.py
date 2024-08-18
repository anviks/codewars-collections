from itertools import permutations


def generate_permutations(size):
    return list(permutations(range(1, size + 1)))


def count_visible_buildings(line):
    return sum(building >= max(line[:index + 1]) for index, building in enumerate(line))


def create_clue_map(size, all_permutations):
    clue_map = {i: set() for i in range(size + 1)}
    for perm in all_permutations:
        clue_map[0].add(perm)
        clue_map[count_visible_buildings(perm)].add(perm)
    return clue_map


def initialize_puzzle_board(size, clue_map, clues):
    top_clues, right_clues = clues[:size], clues[size:size * 2]
    bottom_clues = clues[size * 3 - 1:size * 2 - 1:-1]
    left_clues = clues[size * 4 - 1:size * 3 - 1:-1]

    possible_rows, possible_cols = [], []

    for i in range(size):
        possible_rows.append(clue_map[left_clues[i]].intersection(
            set(tuple(reversed(perm)) for perm in clue_map[right_clues[i]])))
        possible_cols.append(clue_map[top_clues[i]].intersection(
            set(tuple(reversed(perm)) for perm in clue_map[bottom_clues[i]])))

    return possible_rows, possible_cols


def solve_puzzle(clues):
    size = len(clues) // 4
    all_permutations = generate_permutations(size)
    clue_map = create_clue_map(size, all_permutations)

    possible_rows, possible_cols = initialize_puzzle_board(size, clue_map, clues)

    while any(len(row) > 1 for row in possible_rows):
        for row_index in range(size):
            for col_index in range(size):
                valid_combinations = set(row[col_index] for row in possible_rows[row_index]).intersection(
                    set(col[row_index] for col in possible_cols[col_index]))
                possible_rows[row_index] = [row for row in possible_rows[row_index] if
                                            row[col_index] in valid_combinations]
                possible_cols[col_index] = [col for col in possible_cols[col_index] if
                                            col[row_index] in valid_combinations]

    return tuple(tuple(row[0]) for row in possible_rows)
