"""https://www.codewars.com/kata/526156943dfe7ce06200063e"""


class Byte(int):
    def __new__(cls, x=0):
        return super(Byte, cls).__new__(cls, x % 256)

    def __add__(self, other):
        return Byte(super().__add__(other))

    def __sub__(self, other):
        return Byte(super().__sub__(other))


def brain_luck(code, program_input):
    program_input = list(program_input)[::-1]
    cells = [Byte(0)] * 1000
    cell_pointer = 0
    instruction_pointer = 0
    loop_stack = []
    output = ''

    def handle_left():
        nonlocal cell_pointer
        cell_pointer -= 1

    def handle_right():
        nonlocal cell_pointer
        cell_pointer += 1

    def handle_increment():
        cells[cell_pointer] += 1

    def handle_decrement():
        cells[cell_pointer] -= 1

    def handle_output():
        nonlocal output
        output += chr(cells[cell_pointer])

    def handle_input():
        cells[cell_pointer] = Byte(ord(program_input.pop()))

    def handle_loop_start():
        nonlocal instruction_pointer
        if cells[cell_pointer] == 0:
            open_brackets = 1
            while open_brackets != 0:
                instruction_pointer += 1
                if code[instruction_pointer] == '[':
                    open_brackets += 1
                elif code[instruction_pointer] == ']':
                    open_brackets -= 1
        else:
            loop_stack.append(instruction_pointer)

    def handle_loop_end():
        nonlocal instruction_pointer
        if cells[cell_pointer] != 0:
            instruction_pointer = loop_stack[-1]
        else:
            loop_stack.pop()

    instructions = {
        '<': handle_left,
        '>': handle_right,
        '+': handle_increment,
        '-': handle_decrement,
        '.': handle_output,
        ',': handle_input,
        '[': handle_loop_start,
        ']': handle_loop_end,
    }

    while instruction_pointer < len(code):
        instruction = code[instruction_pointer]
        instructions[instruction]()
        instruction_pointer += 1

    return output
