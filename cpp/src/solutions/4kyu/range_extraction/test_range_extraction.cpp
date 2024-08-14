/*
 * https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
 */

#include "solution_range_extraction.hpp"

#include <catch2/catch_all.hpp>

TEST_CASE("Sample_Tests")
{
    SECTION("Tests")
    {
        REQUIRE(range_extraction({-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20}) ==
                "-6,-3-1,3-5,7-11,14,15,17-20");
        REQUIRE(range_extraction({-3, -2, -1, 2, 10, 15, 16, 18, 19, 20}) == "-3--1,2,10,15,16,18-20");
    }

    SECTION("CustomTests")
    {
        REQUIRE(range_extraction({1, 2, 3, 4, 5, 6, 7, 8}) == "1-8");
        REQUIRE(range_extraction({1, 3, 4, 5, 6, 7, 8, 10, 11}) == "1,3-8,10,11");
        REQUIRE(range_extraction({1, 2, 3, 4, 5, 6, 7, 8, 10, 11}) == "1-8,10,11");
        REQUIRE(range_extraction({1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12}) == "1-8,10-12");
        REQUIRE(range_extraction({1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16}) == "1-8,10-12,14-16");
        REQUIRE(range_extraction({1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20}) == "1-8,10-12,14-16,18,20");
        REQUIRE(range_extraction(
                {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}) ==
                "1-8,10-12,14-16,18,20-29");
        REQUIRE(range_extraction({-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20}) ==
                "-6,-3-1,3-5,7-11,14,15,17-20");
        REQUIRE(range_extraction({-3, -2, -1, 2, 10, 15, 16, 18, 19, 20}) == "-3--1,2,10,15,16,18-20");
    }
};

