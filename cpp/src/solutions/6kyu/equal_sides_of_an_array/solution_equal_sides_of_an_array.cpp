/*
 * https://www.codewars.com/kata/5679aa472b8f57fb8c000047
 */

#include "solution_equal_sides_of_an_array.hpp"

#include <vector>
#include <numeric>
#include <vector>

using namespace std;

int find_even_index(const vector<int>& numbers) {
    int left = 0;
    int right = reduce(numbers.begin(), numbers.end(), 0, plus());

    for (int i = 0; i < numbers.size(); i++) {
        right -= numbers[i];
        if (right == left) return i;
        left += numbers[i];
    }

    return -1;
}
