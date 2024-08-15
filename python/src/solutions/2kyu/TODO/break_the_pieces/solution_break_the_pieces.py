"""https://www.codewars.com/kata/break-the-pieces"""

import re


def break_pieces(shape: str):
    broken_shapes = []
    shape_lines = shape.splitlines()
    rows, cols = len(shape_lines), len(shape_lines[0])
    shape_dict = {i + j * 1j: shape_lines[i][j]
                  for i in range(rows)
                  for j in range(cols)
                  if shape_lines[i][j] != ' '}

    pos = 0
    direction = 1
    directions = (1, -1, 1j, -1j)
    positions = [[]]
    intersections = set()

    for m in re.finditer(r'\+', shape):
        intersections.add(complex(*divmod(m.start(), cols + 1)))

    while shape_dict:
        if len(positions[-1]) > 1 and positions[-1][0] == pos:
            if not intersections:
                unique_positions = []
                for pozs in positions:
                    pozs.sort(key=lambda i: (i.real, i.imag))
                    if pozs not in unique_positions:
                        unique_positions.append(pozs)

                zz = [[[' '] * cols for _ in range(rows)] for _ in range(len(unique_positions))]

                for i, pozs in enumerate(unique_positions):
                    for poz in pozs:
                        # print(poz, rows, cols)
                        # print(zz)
                        zz[i][int(poz.real)][int(poz.imag)] = shape_dict[poz]

                return ['\n'.join(rrow for row in rowz if (rrow := ''.join(row).rstrip())) for rowz in zz]

            pos = intersections.pop()

            for d in directions:
                neighbour = pos + d
                if neighbour not in shape_dict:
                    continue
                direction = d
                break

            positions.append([])

        positions[-1].append(pos)

        if shape_dict[pos] != '+':
            pos += direction
            continue

        neighbour_dirs = set()

        for d in directions:
            neighbour = pos + d
            if neighbour not in shape_dict:
                continue
            neighbour_dirs.add(d)

        if len(neighbour_dirs) == 2:
            direction = (neighbour_dirs - {-direction}).pop()
        else:
            if direction / -1j in neighbour_dirs:  # prefer turning left, if not possible, continue straight
                direction /= -1j

        pos += direction

    return broken_shapes

# uncomment next line if you prefer raw error messages
# raw_errors = True
