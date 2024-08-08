//
// Created by Andreas Viks on 11.06.2024.
//

#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <numeric>
#include "range_extraction.h"

using namespace std;

string range_extraction(vector<int> args) {
    vector<int> cache;
    vector<string> result;
    args.push_back(numeric_limits<int>::min());

    for (int arg : args) {
        if (cache.empty() || arg - cache.back() == 1) {
            cache.push_back(arg);
        } else {
            if (cache.size() < 3) {
                for (int num: cache) {
                    result.push_back(to_string(num));
                }
            } else {
                result.push_back(to_string(cache.front()) + "-" + to_string(cache.back()));
            }
            cache.clear();
            cache.push_back(arg);
        }
    }

    if (result.empty()) return "";
    
    return accumulate(result.begin() + 1, result.end(), result[0], 
                      [](const string& x, const string& y) { return x + "," + y; });
}

void test_range_extraction() {
    vector<int> args = {1, 2, 3, 4, 5, 6, 7, 8};
    string result = range_extraction(args);
    string expected = "1-8";
    cout << (result == expected) << " | " << result << endl;

    args = {1, 3, 4, 5, 6, 7, 8, 10, 11};
    result = range_extraction(args);
    expected = "1,3-8,10,11";
    cout << (result == expected) << " | " << result << endl;

    args = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11};
    result = range_extraction(args);
    expected = "1-8,10,11";
    cout << (result == expected) << " | " << result << endl;

    args = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12};
    result = range_extraction(args);
    expected = "1-8,10-12";
    cout << (result == expected) << " | " << result << endl;

    args = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16};
    result = range_extraction(args);
    expected = "1-8,10-12,14-16";
    cout << (result == expected) << " | " << result << endl;

    args = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20};
    result = range_extraction(args);
    expected = "1-8,10-12,14-16,18,20";
    cout << (result == expected) << " | " << result << endl;

    args = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29};
    result = range_extraction(args);
    expected = "1-8,10-12,14-16,18,20-29";
    cout << (result == expected) << " | " << result << endl;

    args = {-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20};
    result = range_extraction(args);
    expected = "-6,-3-1,3-5,7-11,14,15,17-20";
    cout << (result == expected) << " | " << result << endl;

    args = {-3, -2, -1, 2, 10, 15, 16, 18, 19, 20};
    result = range_extraction(args);
    expected = "-3--1,2,10,15,16,18-20";
    cout << (result == expected) << " | " << result << endl;
}
