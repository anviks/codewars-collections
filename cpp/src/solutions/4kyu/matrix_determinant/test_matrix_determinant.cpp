/*
 * https://www.codewars.com/kata/52a382ee44408cea2500074c
 */

#include "solution_matrix_determinant.hpp"

#include <catch2/catch_all.hpp>
#include <iostream>
#include <vector>

using namespace std;

TEST_CASE("your_determinant_function") {
    SECTION("should_work_for_a_few_simple_square_matrices") {
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{1}
        }) == 1);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{1, 3},
                vector<long long>{2, 5}
        }) == -1);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{2, 5, 3},
                vector<long long>{1, -2, -1},
                vector<long long>{1, 3, 4}
        }) == -20);
    }

    SECTION("custom_tests") {
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{1, 2, 3, 4},
                vector<long long>{5, 0, 2, 8},
                vector<long long>{3, 5, 6, 7},
                vector<long long>{2, 5, 3, 1}
        }) == 24);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{-8, 9, -6, 8, -8},
                vector<long long>{2, -6, 9, 1, -8},
                vector<long long>{-4, 7, -9, 4, -4},
                vector<long long>{6, -4, -3, -7, -10},
                vector<long long>{-2, 5, 4, -6, 6}
        }) == -10964);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{10, 10, 1, -5, -5, 9, -10},
                vector<long long>{9, 7, -3, -5, -8, -6, -6},
                vector<long long>{10, 10, -7, 10, -1, 1, -9},
                vector<long long>{5, 5, 4, 8, -10, 9, 10},
                vector<long long>{7, -9, -2, 4, 10, 9, 7},
                vector<long long>{-6, 6, 8, -10, 2, -8, -6},
                vector<long long>{5, -4, -2, 2, -5, 1, 1}
        }) == 36109134);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{7, -3, -5, -8, -6, -6},
                vector<long long>{10, -7, 10, -1, 1, -9},
                vector<long long>{5, 4, 8, -10, 9, 10},
                vector<long long>{-9, -2, 4, 10, 9, 7},
                vector<long long>{6, 8, -10, 2, -8, -6},
                vector<long long>{-4, -2, 2, -5, 1, 1}
        }) == -424102);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{-7, 10, -1, 1, -9},
                vector<long long>{4, 8, -10, 9, 10},
                vector<long long>{-2, 4, 10, 9, 7},
                vector<long long>{8, -10, 2, -8, -6},
                vector<long long>{-2, 2, -5, 1, 1}
        }) == -18938);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{8, -10, 9, 10},
                vector<long long>{4, 10, 9, 7},
                vector<long long>{-10, 2, -8, -6},
                vector<long long>{2, -5, 1, 1}
        }) == -422);
        REQUIRE(determinant(vector<vector<long long> >{
                vector<long long>{10, 9, 7},
                vector<long long>{2, -8, -6},
                vector<long long>{-5, 1, 1}
        }) == -34);
    }
}