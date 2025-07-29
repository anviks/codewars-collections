/*
 * https://www.codewars.com/kata/55905b7597175ffc1a00005a
 */

#include "solution_paginating_a_huge_book.h"

#define ull unsigned long long

ull page_digits(ull pages) {
    ull start = 0, place = 10, result = 0;

    while (pages > start) {
        result += pages - start;
        start = place - 1;
        place *= 10;
    }

    return result;
}
