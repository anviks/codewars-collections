/*
 * https://www.codewars.com/kata/5a90f6d457c5624ecc000012
 */

extern "C" {
#include "solution_next_smaller_pronic.h"
}

#include "../../../test_macros.hpp"
#include <catch2/catch_all.hpp>


void tester(unsigned long long number, unsigned long long expected);

TEST_CASE("next_smaller_pronic:Sample_Tests", "[next_smaller_pronic]") {
    tester(150, 132);
    tester(81, 72);
    tester(49, 42);
    tester(36, 30);
    tester(25, 20);
    tester(16, 12);
    tester(9, 6);
    tester(4, 2);
    tester(2, 0);
    tester(2851579571580622686, 2851579571458726290);
}

void tester(unsigned long long number, unsigned long long expected) {
    unsigned long long submitted = next_smaller_pronic(number);
    char buffer[200];
    snprintf(buffer, 200, "< Incorrect Result >\n \nnumber = %llu\n \nSubmitted: %llu\nExpected:  %llu\n \n",
             number, submitted, expected);
    REQUIRE_MSG(submitted == expected, buffer);
}
