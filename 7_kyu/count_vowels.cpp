//
// Created by Andreas Viks on 22.01.2024.
//

#include "count_vowels.h"
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
