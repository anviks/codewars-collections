def pretty_compare(actual, expected):
    if actual != expected:
        print('\x1B[0;31m', end='')
        sign = '!='
    else:
        print('\x1B[0;32m', end='')
        sign = '=='

    print(repr(actual), sign, end='')
    if len(str(expected)) > 10:
        print('\n', repr(expected), '\x1B[0m', sep='', end='\n\n')
    else:
        print(' ', repr(expected), '\x1B[0m', sep='')
