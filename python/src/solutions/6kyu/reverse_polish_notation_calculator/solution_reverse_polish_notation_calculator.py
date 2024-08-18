"""https://www.codewars.com/kata/52f78966747862fc9a0009ae"""


def calc(expr: str) -> int:
    stack = []

    for token in expr.split(' '):
        if not token:
            break

        if token in '+-*/':
            stack.append(str(eval(f'{stack.pop(-2)} {token} {stack.pop(-1)}')))
        else:
            stack.append(token)

    return stack and eval(stack.pop()) or 0
