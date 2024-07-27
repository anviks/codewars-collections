/**
# [Going to zero or to infinity?](https://www.codewars.com/kata/55a29405bc7d2efaff00007c)

Consider the following numbers (where `n!` is `factorial(n)`):

```
u1 = (1 / 1!) * (1!)
u2 = (1 / 2!) * (1! + 2!)
u3 = (1 / 3!) * (1! + 2! + 3!)
un = (1 / n!) * (1! + 2! + 3! + ... + n!)
```

Which will win: `1 / n!` or `1! + 2! + 3! + ... + n!`?

Are these numbers going to `0` because of `1 / n!` or to infinity due to the sum of factorials?

## Task

Calculate `(1 / n!) * (1! + 2! + 3! + ... + n!)` for a given `n`, where `n` is an integer greater or equal to `1`.

To avoid discussions about rounding, return the result truncated to 6 decimal places, for example:

```
1.0000989217538616 will be truncated to 1.000098
1.2125000000000001 will be truncated to 1.2125
```

## Remark

Keep in mind that factorials grow rather rapidly, and you need to handle large inputs.

## Hint

You could try to simplify the expression.
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

pub fn main() {
    println!("{}", going(5));      // 1.275
    println!("{}", going(6));      // 1.2125
    println!("{}", going(7));      // 1.173214
    println!("{}", going(8));      // 1.146651
    println!("{}", going(9));      // 1.127405
    println!("{}", going(10));     // 1.11274
    println!("{}", going(11));     // 1.101158
    println!("{}", going(12));     // 1.091763
    println!("{}", going(13));     // 1.083981
    println!("{}", going(14));     // 1.077427
    println!("{}", going(15));     // 1.071828
    println!("{}", going(20));     // 1.052786
    println!("{}", going(30));     // 1.034525
    println!("{}", going(50));     // 1.020416
    println!("{}", going(100));    // 1.010102
    println!("{}", going(113));    // 1.008929
    println!("{}", going(200));    // 1.005025
    println!("{}", going(300));    // 1.003344
    println!("{}", going(523));    // 1.001915
    println!("{}", going(1000));   // 1.001001
    println!("{}", going(1011));   // 1.00099
    println!("{}", going(10110));  // 1.000098
}