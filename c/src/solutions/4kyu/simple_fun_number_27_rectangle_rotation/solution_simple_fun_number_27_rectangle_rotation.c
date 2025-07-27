/*
 * https://www.codewars.com/kata/5886e082a836a691340000c3
 */

#include "solution_simple_fun_number_27_rectangle_rotation.h"
#include <math.h>

#define min(a, b) a < b ? a : b
#define max(a, b) a > b ? a : b

long long rectangle_rotation(int a, int b) {
    double A = a * sqrt(2) / 2;
    double B = b * sqrt(2) / 2;
    int count = 0;

    int bound = ceil((A + B) / 2);

    for (int x = -bound; x <= bound; x++) {
        int y_min = ceil(max(-A - x, -B + x));
        int y_max = floor(min(A - x, B + x));

        count += max(0, y_max - y_min + 1);
    }

    return count;
}
