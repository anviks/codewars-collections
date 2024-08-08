//
// Created by Andreas Viks on 29.05.2024.
// https://www.codewars.com/kata/5679aa472b8f57fb8c000047
//

#include "equal_array_sides.h"

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
