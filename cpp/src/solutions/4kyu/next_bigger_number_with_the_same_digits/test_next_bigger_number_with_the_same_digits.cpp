/*
 * https://www.codewars.com/kata/55983863da40caa2c900004e
 */

#include "solution_next_bigger_number_with_the_same_digits.hpp"

#include <catch2/catch_all.hpp>
// TODO: Replace examples and use TDD by writing your own tests

TEST_CASE("NextBiggerNumber")
{
    SECTION("BasicTests")
    {
        REQUIRE(nextBigger(12) == 21);
        REQUIRE(nextBigger(513) == 531);
        REQUIRE(nextBigger(2017) == 2071);
        REQUIRE(nextBigger(414) == 441);
        REQUIRE(nextBigger(144) == 414);
        REQUIRE(nextBigger(10990) == 19009);
    }
};