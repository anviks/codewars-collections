/*
 * https://www.codewars.com/kata/5626b561280a42ecc50000d1
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


// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::sum_dig_pow;
        
    fn dotest(a: u64, b: u64, expected: &[u64]) {
        let actual = sum_dig_pow(a, b);
        assert_eq!(actual, expected, "With a = {a}, b = {b}\nExpected {expected:?} but got {actual:?}")
    }

    #[test]
    fn sample_tests() {
        dotest(1, 10, &[1, 2, 3, 4, 5, 6, 7, 8, 9]);
        dotest(1, 100, &[1, 2, 3, 4, 5, 6, 7, 8, 9, 89]);
        dotest(10, 89, &[89]);
        dotest(10, 100, &[89]);
        dotest(90, 100, &[]);
        dotest(89, 135, &[89, 135]);
        dotest(10, 150, &[89, 135]);
        dotest(12_157_692_622_039_624_753, 12_157_692_622_039_625_615, &[]);
    }
}
