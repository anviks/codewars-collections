/*
 * https://www.codewars.com/kata/55905b7597175ffc1a00005a
 */

extern "C" {
#include "solution_paginating_a_huge_book.h"
}

#include "../../../criterion_wrapper.hpp"

void tester(unsigned long long pages, unsigned long long expected);

Test(page_digits, Sample_Tests) {
    tester(4, 4);
    tester(12, 15);
    tester(100, 192);
}

void tester(unsigned long long pages, unsigned long long expected) {
    unsigned long long submitted = page_digits(pages);
    cr_assert_eq(                                  submitted,       expected,
        "< Incorrect Result >\n \npages = %llu\n \nSubmitted: %llu\nExpected:  %llu\n \n",
                                  pages,           submitted,       expected
    );
}
