import re


def regex_divisible_by(n: int) -> str:
    """
    %18 = %9 %2
    %17 = %17
    %16 = %8 %4 %2
    %15 = %5 %3
    %14 = %7 %2
    %13 = %13
    %12 = %4 %3 %2
    %11 = %11
    %10 = %5 %2
    %9 = %3
    %8 = %4 %2
    %7 = %7
    %6 = %3 %2
    %5 = %5
    %4 = %2
    %3 = %3
    %2 = %2
    """
    if n == 1:
        return '^(0|1)+$'

    exp = 0
    while n % 2 == 0:
        n //= 2
        exp += 1

    m = [['' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i * 2 % n] = '0'
        m[i][(i * 2 + 1) % n] = '1'

    for i in range(n):
        m[i][n - 1] = ''
        m[n - 1][i] = ''

    if n % 2 == 1:
        m[(n - 1) // 2][n - 2] = '01*0'
    else:
        m[n // 2 - 1][n - 2] = '11*0'

    buf_i = ['' for _ in range(n)]
    buf_o = ['' for _ in range(n)]

    for k in range(1, n - 1):
        for i in range(n):
            buf_i[i] = ''
            buf_o[i] = ''

        for i in range(n):
            if m[i][k] != '':
                buf_i[i] = m[i][k]
                m[i][k] = ''

            if m[k][i] != '':
                buf_o[i] = m[k][i]
                m[k][i] = ''

        for i in range(n):
            if buf_i[i] != '':
                for j in range(n):
                    if buf_o[j] != '':
                        if buf_i[k] == '':
                            if m[i][j] == '':
                                m[i][j] = f'({buf_i[i]})({buf_o[j]})'
                            else:
                                m[i][j] = f'({m[i][j]})|({buf_i[i]})({buf_o[j]})'
                        elif i != k:
                            if m[i][j] == '':
                                m[i][j] = f'({buf_i[i]})({buf_i[k]})*({buf_o[j]})'
                            else:
                                m[i][j] = f'({m[i][j]})|({buf_i[i]})({buf_i[k]})*({buf_o[j]})'

    if exp == 0:
        return f'^({m[0][0]})+$'
    elif n == 1:
        return f'^' + '(0|1)*' + '0' * exp + '$'
    else:
        return f'^' + f'({m[0][0]})*' + '0' * (exp + 1) + '$'


if __name__ == '__main__':
    pattern = regex_divisible_by(2)
    for i in range(1, 19):
        pattern = regex_divisible_by(i)
        # assert set(pattern).difference(set("01?:*+^$()[]|")) == set()
        reg = re.compile(pattern)
        # Just a small sample test
        for x in range(5, 13):
            print(bin(x)[2:])
            print(reg.search(bin(x)[2:]))
            assert bool(reg.search(bin(x)[2:])) == (x % i == 0), f'Your result for n={i} was incorrect when matched against {x}'

