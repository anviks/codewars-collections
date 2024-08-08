/*
 * https://www.codewars.com/kata/55a29405bc7d2efaff00007c
 */


fn going(n: i32) -> f64 {
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


#[cfg(test)]
mod tests {
    use super::*;
    use float_eq::float_eq;
    
    fn dotest(n : i32, expected: f64) {
        let actual = going(n);
        let merr = 1.0e-6;
        let res = float_eq!(actual, expected, abs <= merr) || float_eq!(actual, expected, rmax <= merr);
        assert!(res, "For n = {n}\nExpected value must be near: {:e} but was:{:e}", expected, actual);
    }

    #[test]
    fn basics_going() {
        dotest(5, 1.275);
        dotest(6, 1.2125);
        dotest(7, 1.173214);
        dotest(8, 1.146651);
        dotest(9, 1.127405);
        dotest(10, 1.11274);
        dotest(11, 1.101158);
        dotest(12, 1.091763);
        dotest(13, 1.083981);
        dotest(14, 1.077427);
        dotest(15, 1.071828);
        dotest(20, 1.052786);
        dotest(30, 1.034525);
        dotest(50, 1.020416);
        dotest(100, 1.010102);
        dotest(113, 1.008929);
        dotest(200, 1.005025);
        dotest(300, 1.003344);
        dotest(523, 1.001915);
        dotest(1000, 1.001001);
        dotest(1011, 1.00099);
        dotest(10110, 1.000098);
    }
}
