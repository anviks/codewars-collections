"""https://www.codewars.com/kata/58738d518ec3b4bf95000192"""

import re


def expand_commands(match) -> str:
    group_one = match.group(1)
    group_two = int(match.group(2))
    return group_one * group_two


def execute(code: str) -> str:
    pattern = re.compile(r'\(([FRL\d]+)\)(\d+)')

    while pattern.search(code):
        code = pattern.sub(expand_commands, code)

    return roboscript_1_execute(code)


def roboscript_1_execute(code: str) -> str:
    mapper = {'R': 1j, 'L': -1j}
    location = 0
    direction = 1j
    visited: set[complex] = {location}

    for char, multiplier in re.findall(r"([FLR])(\d*)", code):
        multiplier = int(multiplier or 1)

        for _ in range(multiplier):
            if char == 'F':
                location += direction
                visited.add(location)
            else:
                direction /= mapper[char]

    coords = set(map(lambda im: (int(im.real), int(im.imag)), visited))

    min_x = min(coords)[0]
    min_y = min(coords, key=lambda c: c[1])[1]
    max_x = max(coords)[0]
    max_y = max(coords, key=lambda c: c[1])[1]

    matrix = [['*' if complex(x, y) in visited else ' ' for y in range(min_y, max_y + 1)] for x in
              range(min_x, max_x + 1)]

    return '\r\n'.join(''.join(line) for line in matrix)
