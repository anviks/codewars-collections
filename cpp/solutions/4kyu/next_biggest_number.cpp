//
// Created by Andreas Viks on 11.06.2024.
// https://www.codewars.com/kata/55983863da40caa2c900004e
//

#include <iostream>
#include <vector>
#include <algorithm>
#include "next_biggest_number.h"

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

void test_next_biggest_number() {
    long long bigger = nextBigger(12);
    cout << (bigger == 21) << " | " << bigger << endl;
    bigger = nextBigger(513);
    cout << (bigger == 531) << " | " << bigger << endl;
    bigger = nextBigger(2017);
    cout << (bigger == 2071) << " | " << bigger << endl;
    bigger = nextBigger(414);
    cout << (bigger == 441) << " | " << bigger << endl;
    bigger = nextBigger(144);
    cout << (bigger == 414) << " | " << bigger << endl;
    bigger = nextBigger(10990);
    cout << (bigger == 19009) << " | " << bigger << endl;

    bigger = nextBigger(9);
    cout << (bigger == -1) << " | " << bigger << endl;
    bigger = nextBigger(111);
    cout << (bigger == -1) << " | " << bigger << endl;
    bigger = nextBigger(531);
    cout << (bigger == -1) << " | " << bigger << endl;
    
    bigger = nextBigger(59884848459853);
    cout << (bigger == 59884848483559) << " | " << bigger << endl;
}