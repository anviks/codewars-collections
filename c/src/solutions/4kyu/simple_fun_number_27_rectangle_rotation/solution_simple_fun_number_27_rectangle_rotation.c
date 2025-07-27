/*
 * https://www.codewars.com/kata/5886e082a836a691340000c3
 */

#include "solution_simple_fun_number_27_rectangle_rotation.h"
#include <math.h>

long long rectangle_rotation(int a, int b) {
    int c = (a /= sqrt(2)) & 1;
    int d = (b /= sqrt(2)) & 1;

    return (a + !c) * (b + !d) + (a + c) * (b + d);
}
