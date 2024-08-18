/*
 * https://www.codewars.com/kata/57680d0128ed87c94f000bfd
 */

#include "solution_boggle_word_checker.hpp"

#include <catch2/catch_all.hpp>

using namespace std;

TEST_CASE("checks_word")
{
    SECTION("example_test")
    {
        vector<vector<char>> test_board = {
                {'E', 'A', 'R', 'A'},
                {'N', 'L', 'E', 'C'},
                {'I', 'A', 'I', 'S'},
                {'B', 'Y', 'O', 'R'}
        };

        REQUIRE(check_word(test_board, "C") == true);
        REQUIRE(check_word(test_board, "EAR") == true);
        REQUIRE(check_word(test_board, "EARS") == false);
        REQUIRE(check_word(test_board, "BAILER") == true);
        REQUIRE(check_word(test_board, "RSCAREIOYBAILNEA") ==
                true); // Must be able to check indefinite word lengths going in all directions
        REQUIRE(check_word(test_board, "CEREAL") == false); // Valid guesses can't overlap themselves
        REQUIRE(check_word(test_board, "ROBES") == false); // Valid guesses have to be adjacent
        REQUIRE(check_word(test_board, "BAKER") == false); // All the letters have to be in the board
        REQUIRE(check_word(test_board, "CARS") == false); // Valid guesses cannot wrap around the edges of the board
    }
};
