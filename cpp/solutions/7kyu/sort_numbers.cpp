//
// Created by Andreas Viks on 13.01.2024.
//

#include "sort_numbers.h"
#include <vector>
#include <algorithm>

using std::string;

std::vector<int> solution(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end());
    return nums;
}
