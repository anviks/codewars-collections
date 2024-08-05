"""https://www.codewars.com/kata/5a12755832b8b956a9000133"""
import re


class RSUProgram:
    VALID_CHARS = 'FRL()Ppq'

    def __init__(self, source: str):
        self.source = source + '\n'
        self.in_comment = False

    def get_tokens(self):
        tokens = []

        for line in self.source.splitlines(True):
            tokens.extend(self.tokenize_line(line))

        for token in tokens:
            if len(token) > 2:
                if token[1] == '0':
                    raise ValueError(f'Leading zeroes are not allowed ({token!r})')
            elif token in 'Pp':
                raise ValueError('Pattern declarations without identifier are not allowed.')

        return tokens

    def tokenize_line(self, line: str) -> list[str]:
        tokens = []
        current_token = ''

        for char in line:
            if char in '/*':
                if current_token and current_token not in '/*':
                    tokens.append(current_token)
                    current_token = ''
                current_token += char

                if current_token == '//':
                    if self.in_comment:
                        current_token = ''
                    else:
                        return tokens

                if current_token == '/*':
                    current_token = ''
                    self.in_comment = True
                elif current_token == '*/':
                    current_token = ''
                    self.in_comment = False

                continue

            if self.in_comment:
                continue

            if char.isdigit():
                if current_token:
                    current_token += char
                    continue

                raise SyntaxError('Stray numbers')

            if current_token:
                tokens.append(current_token)
                current_token = ''

            if not char.isspace():
                if char not in self.VALID_CHARS:
                    raise ValueError(f'Unknown token: {char!r}')
                current_token = char

        return tokens

    @staticmethod
    def convert_to_raw(tokens: list[str]):
        RSUProgram.validate_syntax(tokens)
        RSUProgram.remove_unreachable_code(tokens)

        tree_constructor = SemanticTreeConstructor()
        tree_constructor.construct_tree(tokens)
        linear_code = tree_constructor.replace_pattern_calls()
        raw_commands = list(RSUProgram.expand_multipliers(''.join(linear_code)))
        unknown_commands = set(raw_commands) - {'F', 'R', 'L'}
        if unknown_commands:
            raise NameError(f'Unknown commands: {unknown_commands}')

        return raw_commands

    @staticmethod
    def validate_syntax(tokens):
        parens = 0
        unclosed_pattern_defs = 0
        for token in tokens:
            if token == '(':
                parens += 1
            elif token[0] == ')':
                parens -= 1
            elif token[0] == 'p':
                if parens != 0:
                    raise SyntaxError('Pattern definitions cannot be in a loop')
                unclosed_pattern_defs += 1
            elif token == 'q':
                unclosed_pattern_defs -= 1
        if unclosed_pattern_defs != 0:
            raise SyntaxError('Unclosed pattern definition')

    @staticmethod
    def remove_unreachable_code(tokens):
        unreachable_ranges = []
        nesting_level = 0
        unreachable_nesting_level = -1
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i][0] == ')':
                if tokens[i] == ')0':
                    if not unreachable_ranges or len(unreachable_ranges[-1]) == 2:
                        unreachable_ranges.append([i + 1])
                        unreachable_nesting_level = nesting_level
                nesting_level += 1
            elif tokens[i] == '(':
                nesting_level -= 1
                if nesting_level == unreachable_nesting_level:
                    unreachable_nesting_level = -1
                    unreachable_ranges[-1].insert(0, i)
        for start, stop in unreachable_ranges:
            tokens[start:stop] = []

    @staticmethod
    def expand_multipliers(code: str) -> str:
        group_pattern = re.compile(r'\(([FRL\d]*)\)(\d*)')
        while group_pattern.search(code):
            code = group_pattern.sub(RSUProgram.expand_match, code)
        code = re.sub(r'([FRL])(\d+)', RSUProgram.expand_match, code)

        return code

    @staticmethod
    def expand_match(match: re.Match) -> str:
        group_one = match.group(1)
        group_two = int(match.group(2) or 1)
        return group_one * group_two

    def execute(self):
        tokens_ = self.get_tokens()
        raw = self.convert_to_raw(tokens_)

        return self.execute_raw(raw)

    @staticmethod
    def execute_raw(cmds):
        mapper = {'R': 1j, 'L': -1j}
        location = 0
        direction = 1j
        visited: set[complex] = {location}

        for char in cmds:
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

        matrix = [['*' if complex(x, y) in visited else ' ' for y in range(min_y, max_y + 1)]
                  for x in range(min_x, max_x + 1)]

        return '\r\n'.join(''.join(line) for line in matrix)


class SemanticTreeConstructor:
    def __init__(self):
        self.tree = {'Global': {'Code': []}}
        self.scope = ['Global']

    def get_scope_tree(self, scope) -> dict:
        tree = self.tree

        for i in range(len(scope)):
            tree = tree.get(scope[i], {})

        return tree

    def find_pattern_scope(self, id_: str, scope: tuple[str]):
        tree = self.tree
        pattern_scope = tuple()

        for i in range(len(scope)):
            tree = tree.get(scope[i], {})
            if id_ in tree:
                pattern_scope = scope[:i + 1] + (id_,)

        return pattern_scope

    def construct_tree(self, tokens):
        for token in tokens:
            if token.startswith('p'):
                pattern_id = token[1:]
                self.enter_scope(pattern_id)
            elif token.startswith('q'):
                self.exit_scope()
            else:
                self.get_scope_tree(self.scope)['Code'].append(token)

    def enter_scope(self, name):
        scope_tree = self.get_scope_tree(self.scope)
        if scope_tree.get(name) is not None:
            raise NameError(f'Pattern {name} already defined in this scope')
        scope_tree[name] = {'Code': []}
        self.scope.append(name)

    def exit_scope(self):
        self.scope.pop()

    def replace_pattern_calls(self, scope=None):
        scope = scope or ('Global',)
        local_tree = self.get_scope_tree(scope)
        tokens = []

        for token in local_tree['Code']:
            if token[0] == 'P':
                pattern_scope = self.find_pattern_scope(token[1:], scope)
                more_tokens = self.replace_pattern_calls(pattern_scope)
                tokens.extend(more_tokens)
            else:
                tokens.append(token)

        return tokens

    def __repr__(self):
        return f"Semantic tree: {self.tree}, Current scope: {self.scope}"


def main():
    with open('roboscript_code_snippets/tests/executor/valid/random_3.txt', encoding='utf-8') as f:
        code_ = f.read()

    parser = RSUProgram(code_)
    print(parser.execute())


if __name__ == '__main__':
    main()
