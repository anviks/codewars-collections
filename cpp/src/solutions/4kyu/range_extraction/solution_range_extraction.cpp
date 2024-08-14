/*
 * https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
 */

#include "solution_range_extraction.hpp"

#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <numeric>

using namespace std;

string range_extraction(vector<int> args) {
    vector<int> cache;
    vector<string> result;
    args.push_back(numeric_limits<int>::min());

    for (int arg: args) {
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
