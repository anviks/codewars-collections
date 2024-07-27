/**
# [Tribonacci Sequence](https://www.codewars.com/kata/556deca17c58da83c00002db)

Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci,
but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with `[1, 1, 1]` as a starting input (AKA signature),
we have this sequence:

```rust
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
```

But what if we started with `[0, 0, 1]` as a signature?
As starting with `[0, 1]` instead of `[1, 1]` basically shifts the common Fibonacci sequence by once place,
you may be tempted to think that we would get the same sequence shifted by 2 places,
but that is not the case and we would get:

```rust
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
```

Well, you may have guessed it by now, but to be clear:
you need to create a fibonacci function that given a signature array/list,
returns the first `n` elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; `n` will always be a non-negative number;
if `n == 0`, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

*[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast
and for showing me this mathematical curiosity too with his usual contagious passion :)]*
 */


fn tribonacci(signature: &[f64; 3], n: usize) -> Vec<f64> {
    let mut vec: Vec<f64> = Vec::with_capacity(n);
    vec.extend_from_slice(
        if n < 3 { &signature[..n] }
        else { signature }
    );

    while vec.len() < n {
        vec.push((vec[vec.len() - 3..]).iter().sum())
    }

    vec
}

pub fn main() {
    println!("{:?}", tribonacci(&[1.0, 1.0, 1.0], 10));  // [1.0, 1.0, 1.0, 3.0, 5.0, 9.0, 17.0, 31.0, 57.0, 105.0]
    println!("{:?}", tribonacci(&[0.0, 0.0, 1.0], 10));  // [0.0, 0.0, 1.0, 1.0, 2.0, 4.0, 7.0, 13.0, 24.0, 44.0]
    println!("{:?}", tribonacci(&[0.5, 0.5, 0.5], 10));  // [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5]
    println!("{:?}", tribonacci(&[0.0, 1.0, 1.0], 10));  // [0.0, 1.0, 1.0, 2.0, 4.0, 7.0, 13.0, 24.0, 44.0, 81.0]
    println!("{:?}", tribonacci(&[1.0, 1.0, 1.0], 1));  // [1.0]
}