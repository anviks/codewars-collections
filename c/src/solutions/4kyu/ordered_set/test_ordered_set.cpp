/*
 * https://www.codewars.com/kata/5c0c5ec84e8f1804b9000296
 */

extern "C" {
#include "solution_ordered_set.h"
}

#include "../../../test_macros.hpp"
#include <catch2/catch_all.hpp>


#include <stdio.h>
#include <stdlib.h>


int int_ascending(const void* a, const void* b) {
    int left = *((int*) a), right = *((int*) b);
    return left - right;
}

char* int_stringizer(const void* a) {
    int value = *((int*) a);
    char* s = (char*) malloc(20 * sizeof(char));
    sprintf(s, "int(%d)", value);
    return s;
}

TEST_CASE("Sample_Tests:Tests", "[Sample_Tests]") {
    Set* set = set_initialize(int_ascending, int_stringizer);
    REQUIRE_MSG(set_size(set) == 0, "Initial size should be 0");

    const int a[] = {5, 1, 8, 0, 6, 3, 7, 9, 2, 4};
    size_t n;
    char buffer[50];

    for (size_t i = 0; i < 10; i++) {
        n = set_size(set);
        REQUIRE_MSG(n == i, "Size before insertion: %ld should be %ld", n, i);
        snprintf(buffer, 50, "%d has not been added yet but was found in the set", a[i]);
        REQUIRE_MSG(!set_includes(set, &a[i]), buffer);

        set_insert(set, &a[i]);

        n = set_size(set);
        REQUIRE_MSG(n == i + 1, "Size after insertion: %ld should be %ld", n, i + 1);
        snprintf(buffer, 50, "%d has just been added but was not found in the set", a[i]);
        REQUIRE_MSG(set_includes(set, &a[i]), buffer);
    }

    for (size_t i = 0; i < 10; i++) {
        n = set_size(set);
        REQUIRE_MSG(n == 10 - i, "Size before deletion: %ld should be %ld", n, 10 - i);
        snprintf(buffer, 50, "%d was added eariler but was not found in the set", a[i]);
        REQUIRE_MSG(set_includes(set, &a[i]), buffer);

        set_remove(set, &a[i]);

        n = set_size(set);
        REQUIRE_MSG(n == 10 - i - 1, "Size after deletion: %ld should be %ld", n, 10 - i - 1);
        snprintf(buffer, 50, "%d has just been removed but was found in the set", a[i]);
        REQUIRE_MSG(!set_includes(set, &a[i]), buffer);
    }
}
