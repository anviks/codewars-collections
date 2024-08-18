# [[Code Golf] Collatz Shortcut Function](https://www.codewars.com/kata/664bb069388167b5923b1688)

The Collatz conjecture states that repeated application of the function
```
f(n) = n / 2 if n is even, 3 * n + 1 if n is odd
```
will eventually reach the value `1` from all positive integer starting values `n`. Because `3 * n + 1` is always even for odd values of `n`, we often use the "shortcut" form of the function instead, defined as
```
g(n) = n / 2 if n is even, (3 * n + 1) / 2 if n is odd.
```

Calculate function `g(n)` in `<= 26` characters, where `1 <= n <= 80_000`.