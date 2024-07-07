"""https://www.codewars.com/kata/assembler-interpreter-part-ii/"""
import re
from operator import add, sub, mul, floordiv, eq, ne, lt, le, gt, ge
from typing import Callable

COMMENT_PATTERN = re.compile(r';.*')
EMPTY_LINE_PATTERN = re.compile(r'(?: *\n)+(?=\n)')  # Find empty lines (empty = contains nothing or only spaces)
LABEL_PATTERN = re.compile(r'(\w+):')
CMD_ARGS_PATTERN = re.compile(r"'[^']*'|[^,\s]+")  # Separate command and arguments

class Assembler:
    def __init__(self):
        self.registers: dict[str, int] = {}  # {register: value}
        self.labels: dict[str, int] = {}  # {label: line_no}
        self._call_stack: list[int] = [0]
        self.lines: list[str] = []
        self.cache = None
        self.output = ''
    
    @property
    def call_stack(self):
        if len(self._call_stack) >= 1000:
            raise RecursionError('Maximum recursion depth exceeded')
        return self._call_stack
    
    @property
    def line_no(self):
        return self._call_stack[-1]
    
    @line_no.setter
    def line_no(self, value):
        self._call_stack[-1] = value

    def get_real_value(self, value: str):
        real_value = self.registers.get(value)
        if real_value is None:
            real_value = int(value)
        return real_value

    def mov(self, reg: str, value: str):
        self.registers[reg] = self.get_real_value(value)

    def inc(self, reg: str):
        self.registers[reg] += 1

    def dec(self, reg: str):
        self.registers[reg] -= 1
        
    def alter_registry_value(self, reg: str, value: str, operation: Callable[[int, int], int]):
        self.registers[reg] = operation(self.registers[reg], self.get_real_value(value))

    add = lambda *args: Assembler.alter_registry_value(*args, operation=add)
    sub = lambda *args: Assembler.alter_registry_value(*args, operation=sub)
    mul = lambda *args: Assembler.alter_registry_value(*args, operation=mul)
    div = lambda *args: Assembler.alter_registry_value(*args, operation=floordiv)

    def jmp(self, label: str):
        self.line_no = self.labels[label]

    def cmp(self, value_a: str, value_b: str):
        self.cache = self.get_real_value(value_a) - self.get_real_value(value_b)

    def jump_if(self, label: str, cmp_func: Callable[[int, int], bool]):
        if cmp_func(self.cache, 0):
            self.jmp(label)
        self.cache = None

    jne = lambda *args: Assembler.jump_if(*args, cmp_func=ne)
    je = lambda *args: Assembler.jump_if(*args, cmp_func=eq)
    jge = lambda *args: Assembler.jump_if(*args, cmp_func=ge)
    jg = lambda *args: Assembler.jump_if(*args, cmp_func=gt)
    jle = lambda *args: Assembler.jump_if(*args, cmp_func=le)
    jl = lambda *args: Assembler.jump_if(*args, cmp_func=lt)
    
    def call(self, label: str):
        self.call_stack.append(self.line_no)
        self.line_no = self.labels[label]
        
    def msg(self, *args):
        for arg in args:
            if arg[0] == arg[-1] == "'":
                self.output += arg[1:-1]
            else:
                self.output += str(self.get_real_value(arg))

    def parse(self, program: str) -> None:
        program = COMMENT_PATTERN.sub('', program)
        program = EMPTY_LINE_PATTERN.sub('', program).strip()

        for label_match in LABEL_PATTERN.finditer(program):
            name = label_match.group(1)
            line_no = program.count('\n', 0, label_match.start())
            self.labels[name] = line_no

        self.lines = [line.strip() for line in program.splitlines()]
        
    def execute(self):
        while self.line_no < len(self.lines):
            current_line = self.lines[self.line_no]
            cmd, *args = CMD_ARGS_PATTERN.findall(current_line)
            
            if not args:
                if cmd == 'ret':
                    self.call_stack.pop()
                elif cmd == 'end':
                    return self.output
            else:
                # This approach implicitly asserts, that command is valid and the correct number of arguments is passed
                getattr(self, cmd)(*args)
                
            self.line_no += 1
            
        return -1


def assembler_interpreter(program: str):
    assembler = Assembler()
    assembler.parse(program)
    
    return assembler.execute()


def main():
    from util_funcs import pretty_compare
    
    def compare_code_output(path, expected_output):
        with open(path) as f:
            pretty_compare(assembler_interpreter(f.read()), expected_output)

    compare_code_output('assembler_code_snippets/simple_program', '(5+1)/2 = 3')
    compare_code_output('assembler_code_snippets/factorial', '5! = 120')
    compare_code_output('assembler_code_snippets/fibonacci', 'Term 8 of Fibonacci series is: 21')
    compare_code_output('assembler_code_snippets/modulo', 'mod(11, 3) = 2')
    compare_code_output('assembler_code_snippets/gcd', 'gcd(81, 153) = 9')
    compare_code_output('assembler_code_snippets/failing', -1)
    compare_code_output('assembler_code_snippets/power', '2^10 = 1024')


if __name__ == '__main__':
    main()
