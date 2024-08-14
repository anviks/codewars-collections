/*
 * https://www.codewars.com/kata/513e08acc600c94f01000001
 */

#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include "solution_rgb_to_hex_conversion.hpp"

using namespace std;

string rgb_to_hex(int r, int g, int b) {
    r = clamp(r, 0, 0xff);
    g = clamp(g, 0, 0xff);
    b = clamp(b, 0, 0xff);

    stringstream stream;
    stream << hex << uppercase << setfill('0')
           << setw(2) << r
           << setw(2) << g
           << setw(2) << b;

    return stream.str();
}
