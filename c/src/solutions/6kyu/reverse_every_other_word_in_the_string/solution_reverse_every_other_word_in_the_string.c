/*
 * https://www.codewars.com/kata/58d76854024c72c3e20000de
 */

#include "solution_reverse_every_other_word_in_the_string.h"

#include <ctype.h>
#include <string.h>

void reverse_word(char* start, char* end) {
    while (start < end) {
        const char temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

char* trimwhitespace(char* str) {
    // Trim leading space
    while (isspace(*str)) str++;

    if (*str == 0)  // Only spaces?
        return str;

    char* end = str + strlen(str) - 1;
    while (end > str && isspace(*end)) end--;

    end[1] = '\0';

    return str;
}

void reverse_alternate(const char* string, char* result) {
    strcpy(result, string);
    const char* trimmed = trimwhitespace(result);
    memmove(result, trimmed, strlen(trimmed) + 1);

    if (strlen(result) > 1) {
        int r;
        int l = r = 1;
        while (result[r] != '\0') {
            if (isspace(result[r]) && isspace(result[r + 1])) {
                while (isspace(result[r + 1])) { r++; }
            }
            result[l] = result[r];
            l++;
            r++;
        }
        result[l] = '\0';
    }

    int spaces = 0;
    char* start = NULL;
    int i;

    for (i = 0; i < strlen(result); ++i) {
        if (isspace(result[i])) {
            if (++spaces % 2 == 1) {
                start = &result[i + 1];
            } else {
                reverse_word(start, &result[i - 1]);
            }
        }
    }

    if (++spaces % 2 != 1) {
        reverse_word(start, &result[i - 1]);
    }

    result[i] = '\0';
}
