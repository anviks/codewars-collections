"""https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111"""


def triangle(row: str):
    row = list(row)
    colours = {'R', 'G', 'B'}

    while len(row) > 1:
        new_row = []

        for i in range(1, len(row)):
            pair_colours = set(row[i - 1:i + 1])
            if len(pair_colours) == 1:
                new_row.append(*pair_colours)
            else:
                new_row.append(*(colours - pair_colours))

        row = new_row

    return row[0]
