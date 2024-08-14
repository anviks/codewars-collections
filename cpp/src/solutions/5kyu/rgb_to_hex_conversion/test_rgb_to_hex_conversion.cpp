/*
 * https://www.codewars.com/kata/513e08acc600c94f01000001
 */

#include "solution_rgb_to_hex_conversion.hpp"
#include <catch2/catch_all.hpp>

TEST_CASE("ExampleTests")
{
    SECTION("BasicTests")
    {
        REQUIRE(rgb_to_hex(0, 0, 0) == "000000");
        REQUIRE(rgb_to_hex(1, 2, 3) == "010203");
        REQUIRE(rgb_to_hex(255, 255, 255) == "FFFFFF");
        REQUIRE(rgb_to_hex(254, 253, 252) == "FEFDFC");
        REQUIRE(rgb_to_hex(-20, 275, 125) == "00FF7D");
    }
};
