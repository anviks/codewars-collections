"""https://www.codewars.com/kata/564057bc348c7200bd0000ff"""


def thirt(n: int) -> int:
    remainders = [1, 10, 9, 12, 3, 4]
    
    while True:
        str_n = str(n)[::-1]
        new_n = 0
        
        for i, d in enumerate(str_n):
            new_n += int(d) * remainders[i % len(remainders)]
            
        if n == new_n: break
        n = new_n
    
    return new_n


def main():
    from util_funcs import pretty_compare

    pretty_compare(thirt(1234567), 87)
    pretty_compare(thirt(8529), 79)
    pretty_compare(thirt(85299258), 31)
    pretty_compare(thirt(5634), 57)
    pretty_compare(thirt(1111111111), 71)
    pretty_compare(thirt(987654321), 30)


if __name__ == '__main__':
    main()
