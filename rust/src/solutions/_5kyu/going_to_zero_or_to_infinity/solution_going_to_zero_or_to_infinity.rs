/*
 * https://www.codewars.com/kata/55a29405bc7d2efaff00007c
 */

pub fn going(n: i32) -> f64 {
    let mut sum = 0.0;

    for i in 1..=n {
        let i = i as f64;
        let mut product = 1.0;
        for j in 1..=n {
            let j = j as f64;
            if j <= i {
                product *= j;
            }
            product *= 1.0 / j;
        }
        sum += product;
    }

    (sum * 1_000_000.0).trunc() / 1_000_000.0
}
