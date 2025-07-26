#ifndef CODEWARS_C_SOLUTION_SORT_BINARY_TREE_BY_LEVELS_H
#define CODEWARS_C_SOLUTION_SORT_BINARY_TREE_BY_LEVELS_H

#include <stddef.h>

typedef struct Tree {
    struct Tree* left;
    struct Tree* right;
    int value;
} Tree;

int* tree_by_levels(const Tree* tree, size_t* tree_size);

#endif  // CODEWARS_C_SOLUTION_SORT_BINARY_TREE_BY_LEVELS_H