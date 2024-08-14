/*
 * https://www.codewars.com/kata/54ff3102c1bad923760001f3
 */

#include "solution_vowel_count.hpp"

#include <catch2/catch_all.hpp>
// TODO: Replace examples and use TDD development by writing your own tests

TEST_CASE("sample_test_cases")
{
    SECTION("test_1")
    {
        REQUIRE(getCount("abracadabra") == 5);
    }
};