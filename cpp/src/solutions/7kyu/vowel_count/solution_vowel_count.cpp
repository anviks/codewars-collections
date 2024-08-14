/*
 * https://www.codewars.com/kata/54ff3102c1bad923760001f3
 */

#include "solution_vowel_count.hpp"

#include <string>

using namespace std;

int getCount(const string &inputStr) {
    int num_vowels = 0;

    for (auto c : inputStr) {
        if ("aeiou"s.find(c) != string::npos) {
            num_vowels++;
        }
    }

    return num_vowels;
}
