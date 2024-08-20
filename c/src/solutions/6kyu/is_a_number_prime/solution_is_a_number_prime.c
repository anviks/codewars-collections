/*
 * https://www.codewars.com/kata/5262119038c0985a5b00029f
 */

#include "solution_is_a_number_prime.h"

#include <stdbool.h>
#include <math.h>

bool is_prime(int num) {
    if (num <= 1) {
        return 0;
    }

    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}
