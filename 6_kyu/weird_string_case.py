"""https://www.codewars.com/kata/52b757663a95b11b3d00062d"""


def to_weird_case(words):
    return ' '.join(''.join(w[i:i + 2].title() for i in range(0, len(words), 2)) for w in words.split())


def main():
    print(to_weird_case('THIs iS a TEST') == 'ThIs Is A TeSt')


if __name__ == '__main__':
    main()
