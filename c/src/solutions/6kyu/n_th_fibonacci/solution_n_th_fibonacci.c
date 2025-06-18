/*
 * https://www.codewars.com/kata/522551eee9abb932420004a0
 */

#include "solution_n_th_fibonacci.h"

typedef unsigned long long ull;

ull nth_fib(const int n) {
    ull a = 0;
    ull b = 1;

    if (n == 1) return a;
    if (n == 2) return b;

    for (int i = 0; i < n - 2; i++) {
        const ull temp = a + b;
        a = b;
        b = temp;
    }

    return b;
}
