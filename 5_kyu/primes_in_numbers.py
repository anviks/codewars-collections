"""https://www.codewars.com/kata/54d512e62a5e54c96200019e"""


def prime_factors(n: int):
    factors = []

    # Check for number of 2s in n
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # n is odd at this point, so step of 2 can be used
    for i in range(3, int(n**0.5) + 1, 2):
        # while i divides n, add i and divide n
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)
    
    result = []
    
    for m in sorted(set(factors)):
        count = factors.count(m)
        if count == 1:
            result += f'({m})'
        else:
            result += f'({m}**{count})'
    
    return ''.join(result)


def main():
    print(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
    print(prime_factors(7919), "(7919)")


if __name__ == '__main__':
    main()

