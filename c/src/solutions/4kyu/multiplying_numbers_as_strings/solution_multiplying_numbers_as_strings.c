/*
 * https://www.codewars.com/kata/55911ef14065454c75000062
 */

#include "solution_multiplying_numbers_as_strings.h"

#include <stdlib.h>
#include <string.h>

char* multiply(const char* a, const char* b) {
    const int a_len = strlen(a);
    const int b_len = strlen(b);
    const int max_len = a_len + b_len;

    // Store multiplication results of singular digits
    int* intermediate_values = calloc((max_len - 1), sizeof(int));

    for (int i = 0; i < a_len; i++) {
        for (int j = 0; j < b_len; j++) {
            intermediate_values[i + j] += (a[i] - '0') * (b[j] - '0');
        }
    }

    char* result = malloc((max_len + 1) * sizeof(char));
    result[max_len] = '\0';

    int carry = 0;

    for (int i = max_len - 2; i >= 0; i--) {
        int digit_sum = intermediate_values[i] + carry;
        result[i + 1] = digit_sum % 10 + '0';
        carry = digit_sum / 10;
    }

    result[0] = carry + '0';

    free(intermediate_values);

    int move_result = 0;

    for (int i = 0; i < max_len - 1; i++) {
        if (result[i] == '0') {
            move_result++;
        } else {
            break;
        }
    }

    memmove(result, result + move_result, max_len + 1 - move_result);

    return result;
}
