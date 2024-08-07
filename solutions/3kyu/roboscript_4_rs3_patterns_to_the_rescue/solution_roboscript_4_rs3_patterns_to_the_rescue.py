"""https://www.codewars.com/kata/594b898169c1d644f900002e"""

import re


def execute(code: str) -> str:
    if re.search(r'p[^q]+p', code):
        raise SyntaxError('Nested patterns are not allowed')

    pattern_pattern = re.compile(r'p(\d+)(.*?)q')
    patterns = {}

    for id_, content in pattern_pattern.findall(code):
        if id_ in patterns:
            raise ValueError('Pattern already exists')

        patterns[id_] = content

    code = pattern_pattern.sub('', code)

    recursion_counter = 0
    while re.search(r'P\d+', code):
        recursion_counter += 1
        code = re.sub(r'P(\d+)', lambda match: patterns[match.group(1)], code)
        if recursion_counter == 1000:
            raise RecursionError('maximum recursion depth exceeded')

    return rs2_execute(code)


def expand_commands(match) -> str:
    group_one = match.group(1)
    group_two = int(match.group(2))
    return group_one * group_two


def rs2_execute(code: str) -> str:
    pattern = re.compile(r'\(([FRL\d]+)\)(\d+)')

    while pattern.search(code):
        code = pattern.sub(expand_commands, code)

    return rs1_execute(code)


def rs1_execute(code: str) -> str:
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
