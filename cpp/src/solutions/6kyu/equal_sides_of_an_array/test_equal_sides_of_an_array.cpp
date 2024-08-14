/*
 * https://www.codewars.com/kata/5679aa472b8f57fb8c000047
 */

#include "solution_equal_sides_of_an_array.hpp"

#include <catch2/catch_all.hpp>
#include <vector>

using namespace std;

TEST_CASE("ShouldPassAllTheTestsProvided")
{
    SECTION("CoreTests")
    {
        {
            vector<int> numbers{1, 2, 3, 4, 3, 2, 1};
            int expected = 3;
            REQUIRE(find_even_index(numbers) == expected);
        }

        {
            vector<int> numbers{1, 100, 50, -51, 1, 1};
            int expected = 1;
            REQUIRE(find_even_index(numbers) == expected);
        }

        {
            vector<int> numbers{1, 2, 3, 4, 5, 6};
            int expected = -1;
            REQUIRE(find_even_index(numbers) == expected);
        }

        {
            vector<int> numbers{20, 10, 30, 10, 10, 15, 35};
            int expected = 3;
            REQUIRE(find_even_index(numbers) == expected);
        }

        {
            vector<int> numbers{20, 10, -80, 10, 10, 15, 35};
            int expected = 0;
            REQUIRE(find_even_index(numbers) == expected);
        }

        {
            vector<int> numbers{10, -80, 10, 10, 15, 35, 20};
            int expected = 6;
            REQUIRE(find_even_index(numbers) == expected);
        }

        {
            vector<int> numbers{0, 0, 0, 0, 0};
            int expected = 0;
            REQUIRE(find_even_index(numbers) == expected);
        }

        {
            vector<int> numbers{-1, -2, -3, -4, -3, -2, -1};
            int expected = 3;
            REQUIRE(find_even_index(numbers) == expected);
        }
    }
};
