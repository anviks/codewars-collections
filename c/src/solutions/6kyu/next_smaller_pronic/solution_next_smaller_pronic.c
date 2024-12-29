/*
 * https://www.codewars.com/kata/5a90f6d457c5624ecc000012
 */

#include "solution_next_smaller_pronic.h"

#include <math.h>

unsigned long long next_smaller_pronic(unsigned long long number) {
    unsigned long long n = (unsigned long long)round(sqrt(number));
    return (n - 1) * n;
}
