/*
 * https://www.codewars.com/kata/51b6249c4612257ac0000005
 */

pub fn roman_as_num(roman: &str) -> u64 {
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
