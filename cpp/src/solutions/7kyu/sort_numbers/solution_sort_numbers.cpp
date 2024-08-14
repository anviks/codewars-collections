/*
 * https://www.codewars.com/kata/5174a4c0f2769dd8b1000003
 */

#include "solution_sort_numbers.hpp"

#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> nums) {
    sort(nums.begin(), nums.end());
    return nums;
}

