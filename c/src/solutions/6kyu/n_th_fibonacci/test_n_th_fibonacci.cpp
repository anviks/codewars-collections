/*
 * https://www.codewars.com/kata/522551eee9abb932420004a0
 */

#include "solution_n_th_fibonacci.h"

#include "../../../criterion_wrapper.hpp"

typedef unsigned long long ull;

ull nth_fib(int n);

static void tester(int n, ull expected) {
    ull submitted = nth_fib(n);
    cr_assert_eq(submitted, expected,
        "For n = %d\n \n Submitted: %llu\n \n Expected:  %llu\n \n",
             n,          submitted,           expected);
}

Test(Example_Tests, should_pass_all_the_tests_provided) {
    tester(1, 0);
    tester(2, 1);
    tester(3, 1);
    tester(4, 2);
    tester(5, 3);
    tester(6, 5);
    tester(7, 8);
    tester(8, 13);
    tester(9, 21);
    tester(10, 34);
    tester(11, 55);
    tester(12, 89);
    tester(13, 144);
    tester(14, 233);
    tester(15, 377);
    tester(16, 610);
    tester(17, 987);
    tester(18, 1597);
    tester(19, 2584);
    tester(20, 4181);
    tester(21, 6765);
    tester(22, 10946);
    tester(23, 17711);
    tester(24, 28657);
    tester(25, 46368);
}
