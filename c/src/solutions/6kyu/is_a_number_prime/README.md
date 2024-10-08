# [Is a number prime?](https://www.codewars.com/kata/5262119038c0985a5b00029f)

Define a function that takes an integer argument and returns a logical value `true` or `false` depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than `1` that has no positive divisors other than `1` and itself.

## Requirements

* You can assume you will be given an integer input.
* You can not assume that the integer will be only positive. You may be given negative numbers as well ( or `0` ).
* **NOTE on performance**: There are no fancy optimizations required, but still _the_ most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to `n`, or `n/2`, will be too slow.

## Example

```c
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
```
```c++
bool isPrime(5) = return true
```
## Encodings

purity: `LetRec`  
numEncoding: `BinaryScott` ( so, no negative numbers )  
export deconstructor `if` for your `Boolean` encoding  
