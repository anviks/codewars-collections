/**
# [Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!](https://www.codewars.com/kata/5626b561280a42ecc50000d1)

The number `89` is the first integer with more than one digit that fulfills the property
partially introduced in the title of this kata.
What's the use of saying "Eureka"? Because this sum gives the same number: `89 = 8^1 + 9^2`

The next number in having this property is `135`.

See this property again: `135 = 1^1 + 3^2 + 5^3`

## Task

We need a function `sum_dig_pow()` to collect these numbers, that may receive two integers
`a`, `b` that defines the range `[a, b]` (inclusive) and outputs a list of the sorted
numbers in the range that fulfills the property described above.

## Examples

```rust
sum_dig_pow(1, 10)  // [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_dig_pow(1, 100)  // [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
sum_dig_pow(10, 100)  //  [89]
sum_dig_pow(90, 100)  // []
```

## Notes

- If there are no numbers of this kind in the range `[a, b]` the function should output an empty list.
- The same happens if the result is greater than `b`.

## Kata in this Series

- [Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!](https://www.codewars.com/kata/5626b561280a42ecc50000d1)
- [Last digits of N^2 equal to 1](https://www.codewars.com/kata/5511b2f550906349a70004e1)
- [Digits sequence](https://www.codewars.com/kata/5a057ec846d843c81a0000ad)
*/


fn sum_dig_pow(a: u64, b: u64) -> Vec<u64> {
    (a..=b).filter(|&u| u == raise_digits(u)).collect()
}

fn raise_digits(n: u64) -> u64 {
    let mut result: u64 = 0;
    let string_n = n.to_string();
    let mut chars = string_n.chars();

    for i in 0..string_n.len() {
        result += u64::pow(chars.nth(0).unwrap().to_digit(10).unwrap() as u64, (i + 1) as u32);
    }

    result
}


pub fn main() {
    println!("{:?}", sum_dig_pow(1, 9));  // [1, 2, 3, 4, 5, 6, 7, 8, 9]
    println!("{:?}", sum_dig_pow(1, 100));  // [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    println!("{:?}", sum_dig_pow(10, 100));  //  [89]
    println!("{:?}", sum_dig_pow(90, 100));  // []
    println!("{:?}", sum_dig_pow(90, 150));  // [135]
    println!("{:?}", sum_dig_pow(50, 150));  // [89, 135]
    println!("{:?}", sum_dig_pow(10, 150));  // [89, 135]
    println!("{:?}", sum_dig_pow(12157692622039624753, 12_157_692_622_039_625_615));  // []
}
