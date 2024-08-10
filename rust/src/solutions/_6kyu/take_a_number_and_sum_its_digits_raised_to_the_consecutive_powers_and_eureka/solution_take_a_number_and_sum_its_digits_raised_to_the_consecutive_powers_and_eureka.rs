/*
 * https://www.codewars.com/kata/5626b561280a42ecc50000d1
 */

pub fn sum_dig_pow(a: u64, b: u64) -> Vec<u64> {
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

