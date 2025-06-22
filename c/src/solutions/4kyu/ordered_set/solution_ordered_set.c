/*
 * https://www.codewars.com/kata/5c0c5ec84e8f1804b9000296
 */

#include "solution_ordered_set.h"

#include <stdlib.h>
#include <string.h>

typedef int (* Comparator)(const void*, const void*);

typedef char*(* Stringizer)(const void*);

struct Set {
    void** stuff;
    size_t size;
    size_t capacity;

    Comparator comparator;
    Stringizer stringizer;
};

unsigned int get_insertion_index(const Set* set, const void* item) {
    if (set->size == 0) {
        return 0;
    }

    unsigned int low = 0, high = set->size - 1;

    while (low <= high) {
        const unsigned int mid = low + (high - low) / 2;
        const int comparison = set->comparator(set->stuff[mid], item);

        if (comparison == 0) {
            return mid;
        }

        if (comparison < 0) {
            low = mid + 1;
        } else {
            if (mid == 0) return low;
            high = mid - 1;
        }
    }

    return low;
}

Set* set_initialize(Comparator comparator, Stringizer stringizer) {
    Set* set = malloc(sizeof(Set));

    set->size = 0;
    set->capacity = 100;
    set->stuff = calloc(set->capacity, sizeof(void*));
    set->comparator = comparator;
    set->stringizer = stringizer;

    return set;
}

void set_destroy(Set* set) {
    free(set->stuff);
    free(set);
}

size_t set_size(const Set* set) {
    return set->size;
}

int set_includes(const Set* set, const void* item) {
    unsigned int index = get_insertion_index(set, item);

    return index < set->size && set->comparator(set->stuff[index], item) == 0;
}

void check_capacity(Set* set) {
    if (set->size == set->capacity) {
        set->capacity += 100;
    } else if (set->capacity - set->size >= 200) {
        set->capacity -= 100;
    } else {
        return;
    }
    void** newStuff = realloc(set->stuff, set->capacity * sizeof(void*));
    if (!newStuff) {
        exit(EXIT_FAILURE);
    }
    set->stuff = newStuff;
}

void set_insert(Set* set, const void* item) {
    unsigned int index = get_insertion_index(set, item);

    if (index >= set->size) {
        set->stuff[index] = item;
    } else if (set->comparator(set->stuff[index], item) == 0) {
        return;
    } else {
        memmove(set->stuff + index + 1, set->stuff + index, (set->size - index) * sizeof(void*));
        set->stuff[index] = item;
    }

    set->size++;
    check_capacity(set);
}

void set_remove(Set* set, const void* item) {
    if (set->size == 0) return;

    unsigned int index = get_insertion_index(set, item);

    if (index >= set->size) return;

    if (set->comparator(set->stuff[index], item) == 0) {
        memmove(set->stuff + index, set->stuff + index + 1, (set->size - index - 1) * sizeof(void*));
        set->size--;
        check_capacity(set);
    }
}
