/*
 * https://www.codewars.com/kata/5a90f6d457c5624ecc000012
 */

#include "solution_next_smaller_pronic.h"

#include "../../../criterion_wrapper.hpp"

unsigned long long next_smaller_pronic(unsigned long long number);
static void tester(unsigned long long number, unsigned long long expected);

Test(next_smaller_pronic, Sample_Tests) {
    tester(150, 132);
    tester(81, 72);
    tester(49, 42);
    tester(36, 30);
    tester(25, 20);
    tester(16, 12);
    tester(9, 6);
    tester(4, 2);
    tester(2, 0);
}

static void tester(unsigned long long number, unsigned long long expected) {
    unsigned long long submitted = next_smaller_pronic(number);
    cr_assert_eq(                                   submitted,       expected,
        "< Incorrect Result >\n \nnumber = %llu\n \nSubmitted: %llu\nExpected:  %llu\n \n",
                                  number,           submitted,       expected
    );
}
