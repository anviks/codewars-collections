/*
 * https://www.codewars.com/kata/542c0f198e077084c0000c2e
 */

#include "solution_count_the_divisors_of_a_number.hpp"

#include <catch2/catch_all.hpp>
TEST_CASE("Count_divisors")
{
    SECTION("Fixed_tests")
    {
        REQUIRE(divisors(1) == (1));
        REQUIRE(divisors(4) == (3));
        REQUIRE(divisors(5) == (2));
        REQUIRE(divisors(12) == (6));
        REQUIRE(divisors(25) == (3));
        REQUIRE(divisors(30) == (8));
        REQUIRE(divisors(4096) == (13));
    }
};
