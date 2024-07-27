/**
# [Roman Numerals Decoder](https://www.codewars.com/kata/51b6249c4612257ac0000005)

Create a function that takes a Roman numeral as its argument
and returns its value as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
starting with the leftmost digit and skipping any 0s.
So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC)
and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

```rust
solution("XXI"); // should return 21
```

Help:

```rust
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
```
 */


fn roman_as_num(roman: &str) -> u64 {
    let mut result = 0;
    let mut prev_value: u64 = 1001;

    for c in roman.chars() {
        let value = match c {
            'M' => 1000,
            'D' => 500,
            'C' => 100,
            'L' => 50,
            'X' => 10,
            'V' => 5,
            'I' => 1,
            _ => continue
        };

        result += value;

        if value > prev_value {
            result -= 2 * prev_value
        }

        prev_value = value
    }

    result
}

pub fn main() {
    println!("{}", roman_as_num("XXI"));  // 21
    println!("{}", roman_as_num("I"));  // 1
    println!("{}", roman_as_num("IV"));  // 4
    println!("{}", roman_as_num("MMVIII"));  // 2008
    println!("{}", roman_as_num("MDCLXVI"));  // 1666
}
