"""https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4"""


def is_prime(n: int) -> bool:
    return next((False for m in range(2, int(n ** 0.5) + 1) if n % m == 0), True)


def gap(g: int, m: int, n: int) -> list[int] | None:
    primes = []
    
    for num in range(m, n + 1):
        if is_prime(num):
            primes.append(num)
            if len(primes) > 1 and primes[-1] - primes[-2] == g:
                return primes[-2:]
    
    return None


def main():
    from util_funcs import pretty_compare

    pretty_compare(gap(2, 100, 110), [101, 103])
    pretty_compare(gap(4, 100, 110), [103, 107])
    pretty_compare(gap(6, 100, 110), None)
    pretty_compare(gap(8, 300, 400), [359, 367])
    pretty_compare(gap(10, 300, 400), [337, 347])
    pretty_compare(gap(2, 100, 103), [101, 103])


if __name__ == '__main__':
    main()
