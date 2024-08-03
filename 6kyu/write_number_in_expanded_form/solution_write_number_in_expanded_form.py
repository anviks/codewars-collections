"""https://www.codewars.com/kata/5842df8ccbd22792a4000245"""


def expanded_form(num):
    return ' + '.join([str(int(d) * 10 ** i) for i, d in enumerate(str(num)[::-1]) if d != '0'][::-1])


def expanded_form(n):
    return (m := len(s := str(n))) and ' + '.join(x + '0' * (m - i) for i, x in enumerate(s, 1) if x != '0')
