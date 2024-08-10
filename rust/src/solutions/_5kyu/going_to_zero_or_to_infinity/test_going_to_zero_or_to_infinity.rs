/*
 * https://www.codewars.com/kata/55a29405bc7d2efaff00007c
 */

#[cfg(test)]
mod tests {
    use float_eq::float_eq;
    use crate::solutions::_5kyu::going_to_zero_or_to_infinity::solution_going_to_zero_or_to_infinity::going;

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
    }
}
