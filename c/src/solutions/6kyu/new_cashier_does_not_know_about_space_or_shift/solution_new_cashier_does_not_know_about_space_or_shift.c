/*
 * https://www.codewars.com/kata/5d23d89906f92a00267bb83d
 */

#include "solution_new_cashier_does_not_know_about_space_or_shift.h"

#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int count_occurrences(const char* haystack, char* needle) {
    int occurrences = 0;
    char* lowerNeedle = malloc(strlen(needle) + 1);
    strcpy(lowerNeedle, needle);
    lowerNeedle[0] = tolower(lowerNeedle[0]);
    size_t window_size = strlen(lowerNeedle);

    for (size_t i = 0; i < strlen(haystack) - window_size + 1; ++i) {
        for (int j = 0; j < window_size; ++j) {
            if (haystack[i + j] != lowerNeedle[j]) goto not_found;
        }
        occurrences++;
        not_found:;
    }

    free(lowerNeedle);

    return occurrences;
}

char* get_order(const char* input) {
    const char* items[] = {"Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"};
    char* output = malloc(strlen(input) * 2);
    output[0] = '\0';

    for (int i = 0; i < 8; ++i) {
        const char* item = items[i];
        int occ = count_occurrences(input, item);

        for (int j = 0; j < occ; ++j) {
            strcat(output, item);
            strcat(output, " ");
        }
    }

    if (strlen(output) > 0) output[strlen(output) - 1] = '\0';

    return output;
}
