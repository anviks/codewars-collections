/*
 * https://www.codewars.com/kata/5174a4c0f2769dd8b1000003
 */

#include "solution_sort_numbers.hpp"

#include <catch2/catch_all.hpp>
#include <vector>

typedef std::vector<int> v;

TEST_CASE("Advanced_Tests")
{
    SECTION("advanced_tests")
    {
        REQUIRE(solution({1, 2, 3, 10, 5}) == v{1, 2, 3, 5, 10});
        REQUIRE(solution({}) == (v{}));
        REQUIRE(solution({20, 2, 10}) == v{2, 10, 20});
        REQUIRE(solution({2, 20, 10}) == v{2, 10, 20});
    }
};
