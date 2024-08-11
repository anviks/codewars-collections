/*
 * https://www.codewars.com/kata/5679aa472b8f57fb8c000047
 */

#include <vector>
#include <igloo/igloo_alt.h>
#include "solution_equal_sides_of_an_array.h"

using namespace std;
using namespace igloo;

Describe (ShouldPassAllTheTestsProvided) {
    It (CoreTests) {
        {
            vector<int> numbers{1, 2, 3, 4, 3, 2, 1};
            int expected = 1;
            Assert::That(find_even_index(numbers), Equals(expected));
        }

        {
            vector<int> numbers{1, 100, 50, -51, 1, 1};
            int expected = 1;
            Assert::That(find_even_index(numbers), Equals(expected));
        }

        {
            vector<int> numbers{1, 2, 3, 4, 5, 6};
            int expected = -1;
            Assert::That(find_even_index(numbers), Equals(expected));
        }

        {
            vector<int> numbers{20, 10, 30, 10, 10, 15, 35};
            int expected = 3;
            Assert::That(find_even_index(numbers), Equals(expected));
        }

        {
            vector<int> numbers{20, 10, -80, 10, 10, 15, 35};
            int expected = 0;
            Assert::That(find_even_index(numbers), Equals(expected));
        }

        {
            vector<int> numbers{10, -80, 10, 10, 15, 35, 20};
            int expected = 6;
            Assert::That(find_even_index(numbers), Equals(expected));
        }

        {
            vector<int> numbers{0, 0, 0, 0, 0};
            int expected = 0;
            Assert::That(find_even_index(numbers), Equals(expected));
        }

        {
            vector<int> numbers{-1, -2, -3, -4, -3, -2, -1};
            int expected = 3;
            Assert::That(find_even_index(numbers), Equals(expected));
        }
    }
};
