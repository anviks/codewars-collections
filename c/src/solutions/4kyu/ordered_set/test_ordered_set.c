/*
 * https://www.codewars.com/kata/5c0c5ec84e8f1804b9000296
 */

#include "solution_ordered_set.h"

#include <criterion/criterion.h>
#include <stdio.h>
#include <stdlib.h>

typedef int (*Comparator)(const void*, const void*);
typedef char* (*Stringizer)(const void*);

Set* set_initialize(Comparator, Stringizer);
void set_destroy(Set*);
size_t set_size(const Set*);
int set_includes(const Set*, const void*);
void set_insert(Set*, const void*);
void set_remove(Set*, const void*);

int int_ascending(const void* a, const void* b) {
    int left = *((int*)a), right = *((int*)b);
    return left - right;
}

char* int_stringizer(const void* a) {
    int value = *((int*)a);
    char* s = calloc(16, sizeof(char));
    sprintf(s, "int(%d)", value);
    return s;
}

Test(Sample_Tests, Tests) {
    Set* set = set_initialize(int_ascending, int_stringizer);
    cr_assert_eq(set_size(set), 0, "Initial size should be 0");

    const int a[] = {5, 1, 8, 0, 6, 3, 7, 9, 2, 4};
    size_t n;

    for (size_t i = 0; i < 10; i++) {
        n = set_size(set);
        cr_assert_eq(n, i, "Size before insertion: %ld should be %ld", n, i);
        cr_assert_not(set_includes(set, &a[i]), "%d has not been added yet but was found in the set", a[i]);

        set_insert(set, &a[i]);

        n = set_size(set);
        cr_assert_eq(n, i + 1, "Size after insertion: %ld should be %ld", n, i + 1);
        cr_assert(set_includes(set, &a[i]), "%d has just been added but was not found in the set", a[i]);
    }

    for (size_t i = 0; i < 10; i++) {
        n = set_size(set);
        cr_assert_eq(n, 10 - i, "Size before deletion: %ld should be %ld", n, 10 - i);
        cr_assert(set_includes(set, &a[i]), "%d was added eariler but was not found in the set", a[i]);

        set_remove(set, &a[i]);

        n = set_size(set);
        cr_assert_eq(n, 10 - i - 1, "Size after deletion: %ld should be %ld", n, 10 - i - 1);
        cr_assert_not(set_includes(set, &a[i]), "%d has just been removed but was found in the set", a[i]);
    }
}
