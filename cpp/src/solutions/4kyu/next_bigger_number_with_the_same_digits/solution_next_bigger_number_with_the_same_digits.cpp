/*
 * https://www.codewars.com/kata/55983863da40caa2c900004e
 */

#include "solution_next_bigger_number_with_the_same_digits.hpp"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long nextBigger(long long n) {
    vector<int> digits;

    for (int i = (int) log10(n); i >= 0; i--) {
        int val = n / (long long) pow(10, i) % 10;
        digits.push_back(val);
    }

    bool result = next_permutation(digits.begin(), digits.end());

    if (!result) return -1;

    long long final_num = 0;

    for (int i = 0; i < digits.size(); i++) {
        final_num += (long long) (digits[i] * pow(10, digits.size() - i - 1));
    }

    return final_num;
}