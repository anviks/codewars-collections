/*
 * https://www.codewars.com/kata/525f4206b73515bffb000b21
 */

#include "solution_adding_big_numbers.h"

#include <stdlib.h>
#include <string.h>

char* add(const char* a, const char* b) {
    if (strlen(a) < strlen(b)) {
        const char* temp = a;
        a = b;
        b = temp;
    }

    const size_t longer = strlen(a);
    const size_t shorter = strlen(b);

    int carry = 0;
    char* result = malloc(longer + 2);
    result[longer + 1] = '\0';

    for (int i = 0; i < longer; ++i) {
        const char first = a[longer - i - 1];
        const char second = i < shorter ? b[shorter - i - 1] : '0';

        int sum = first + second + carry - '0' - '0';

        carry = sum > 9;
        sum %= 10;

        result[longer - i] = (char)(sum + '0');
    }

    if (carry) {
        result[0] = '1';
    } else {
        memmove(result, result + 1, longer + 1);
    }

    return result;
}
