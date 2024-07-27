/**
# [ISBN-10 Validation](https://www.codewars.com/kata/51fc12de24a9d8cb0e000001)

ISBN-10 identifiers are ten digits long. The first nine characters are digits `0-9`.
The last digit can be `0-9` or `X`, to indicate a value of `10`.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:

```rust
ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
```

This is a valid ISBN, because:

```rust
(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
```

## Examples

```rust
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false
```
 */


use regex::Regex;


fn valid_isbn10(isbn: &str) -> bool {
    let pattern = r"^\d{9}(?:\d|X)$";
    let regex = Regex::new(pattern).unwrap();

    match regex.find(isbn) {
        None => return false,
        _ => ()
    }

    let sum = isbn.chars()
        .into_iter()
        .enumerate()
        .fold(0, |acc, (index, c)| acc + (index + 1) as u32 * c.to_digit(10).unwrap_or(10));

    sum % 11 == 0
}

pub fn main() {
    println!("{}", valid_isbn10("1112223339"));   // true
    println!("{}", valid_isbn10("111222333"));    // false
    println!("{}", valid_isbn10("1112223339X"));  // false
    println!("{}", valid_isbn10("1234554321"));   // true
    println!("{}", valid_isbn10("1234512345"));   // false
    println!("{}", valid_isbn10("048665088X"));   // true
    println!("{}", valid_isbn10("X123456788"));   // false
}