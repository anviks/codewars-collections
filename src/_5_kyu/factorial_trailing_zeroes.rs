/**
# [Number of trailing zeros of N!](https://www.codewars.com/kata/52f787eb172a8b4ae1000a34)

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

`N! = 1 * 2 * 3 * ... * N`

Be careful `1000!` has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

## Examples
```rust
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
```

*Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.*
*/


fn zeros(n: u64) -> u64 {
    let r = n / 5;
    if r >= 5 { return zeros(r) + r; }
    return r;
}

pub fn main() {
    println!("{}", zeros(0));  // 0
    println!("{}", zeros(6));  // 1
    println!("{}", zeros(14)); // 2
    println!("{}", zeros(30)); // 7
    println!("{}", zeros(100)); // 24
    println!("{}", zeros(1000)); // 249
    println!("{}", zeros(100000)); // 24999
    println!("{}", zeros(1000000000)); // 249999998
    println!("{}", zeros(1000000000000)); // 249999999997
}