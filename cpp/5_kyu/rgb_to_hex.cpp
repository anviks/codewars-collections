//
// Created by Andreas Viks on 30.05.2024.
//

#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include "rgb_to_hex.h"

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

void test_rgb() {
    cout << rgb_to_hex(  1,  2,  3) << endl;  // 010203
    cout << rgb_to_hex(254,253,252) << endl;  // FEFDFC
    cout << rgb_to_hex(-20,275,125) << endl;  // 00FF7D
}

