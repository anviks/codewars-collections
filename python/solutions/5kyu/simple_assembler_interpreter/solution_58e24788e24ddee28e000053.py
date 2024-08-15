"""https://www.codewars.com/kata/simple-assembler-interpreter"""


def simple_assembler(program: list[str]) -> dict[str, int]:
    registers: dict[str, int] = {}
    current_line_no = 0

    def get_real_value(value: str):
        real_value = registers.get(value)
        if real_value is None:
            real_value = int(value)
        return real_value

    def handle_mov(reg: str, value: str):
        registers[reg] = get_real_value(value)

    def handle_inc(reg: str):
        registers[reg] += 1

    def handle_dec(reg: str):
        registers[reg] -= 1

    def handle_jnz(value: str, steps: str):
        nonlocal current_line_no
        if get_real_value(value) != 0:
            current_line_no += int(steps) - 1  # Subtract 1 because the loop will increment it by 1

    while current_line_no < len(program):
        current_line = program[current_line_no]
        cmd, *args = current_line.split()
        # This function approach implicitly asserts, that command is valid and the correct number of arguments is passed
        locals().get(f'handle_{cmd}')(*args)
        current_line_no += 1

    return registers
