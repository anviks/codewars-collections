/*
 * https://www.codewars.com/kata/542c0f198e077084c0000c2e
 */

#include "solution_count_the_divisors_of_a_number.hpp"
#include <cmath>

using namespace std;

int divisors(int n) {
    double n_root = sqrt(n);
    int count = 0;

    for (int i = 1; i < n_root; ++i) {
        if (!(n % i)) {
            count += 2;
        }
    }

    return count + (n_root == (int) n_root);
}

