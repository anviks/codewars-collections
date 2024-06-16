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


def main():
    # print(execute("p1F2Lqp2F2Rqp3P1(P2)2P1q(P3)3"))

    # p1F2Lqp2F2Rqp3P1(P2)2P1q(P3)3
    # F2LF2RF2RF2LF2LF2RF2RF2LF2LF2RF2RF2L
    
    # execute("p1F2Lqp1(F3LF4R)5qp2F2Rqp3P1(P2)2P1q(P3)3")  # Exception
    
    # print(execute('R9FR7R1L8((F3RF5L)0R(F7LF6LF1R6)8LR1F(F1LF2LF9R8)10R2L1R)5L8F4LL8F'))
    # execute("RL66RRFR7F73R69FFFFFLRRR71FRRL34R81FLR97F20LL61RLL5R17LF26F84FR71L83F26FRR46FF16FR22LLL1RRR49F71RRR54L50RF75LL94FRL98FF55FLL28R71R8FRFFF86LRR50RRR50FFL10R23FR97L9LFLFFFFLRL8R")
    # execute("F5LF5LF5LF5L")


    # F4LF4RF4RF4LF4LF4RF4RF4LF4LF4RF4RF4
    # F4L((F4R)2(F4L)2)2(F4R)2F4    
    pass


if __name__ == '__main__':
    main()
