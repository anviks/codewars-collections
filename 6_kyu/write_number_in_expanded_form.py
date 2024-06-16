def expanded_form(num):        
    return ' + '.join([str(int(d) * 10 ** i) for i, d in enumerate(str(num)[::-1]) if d != '0'][::-1])

def expanded_form(n):
    return (m := len(s := str(n))) and ' + '.join(x + '0' * (m - i) for i, x in enumerate(s, 1) if x != '0')


def main():
    print(expanded_form(12))
    print(expanded_form(42))
    print(expanded_form(70304))


if __name__ == '__main__':
    main()
