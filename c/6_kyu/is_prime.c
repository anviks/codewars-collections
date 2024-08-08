#include <stdbool.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * <a href="https://www.codewars.com/kata/5262119038c0985a5b00029f"><h2>Is a number prime?</h2></a>
 * <p>
 * Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.
 * <p>
 * Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
 * <p>
 * Requirements:
 * <ul>
 *    <li>You can assume you will be given an integer input.</li>
 *    <li>You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).</li>
 *    <li>NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
 *    Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.</li>
 * </ul>
 * <p>
 * <h3>Examples:</h3>
 * <pre>
 * <code>is_prime(1)  // false</code><br>
 * <code>is_prime(2)  // true</code><br>
 * <code>is_prime(-1) // false</code><br>
 * </pre>
 * </p>
 */
bool is_prime(int num) {
    if (num <= 1) {
        return 0;
    }

    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}


void run() {
    printf("%d\n", is_prime(1));  // false
    printf("%d\n", is_prime(2));  // true
    printf("%d\n", is_prime(-1)); // false
    printf("%d\n", is_prime(3));  // true
    printf("%d\n", is_prime(5));  // true
    printf("%d\n", is_prime(7));  // true
    printf("%d\n", is_prime(41)); // true
    printf("%d\n", is_prime(5099)); // true
    printf("%d\n", is_prime(4));  // false
    printf("%d\n", is_prime(6));  // false
    printf("%d\n", is_prime(8));  // false
}
