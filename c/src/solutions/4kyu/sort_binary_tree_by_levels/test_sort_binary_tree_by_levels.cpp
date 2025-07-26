/*
 * https://www.codewars.com/kata/52bef5e3588c56132c0003bc
 */

extern "C" {
#include "solution_sort_binary_tree_by_levels.h"
}

#include "../../../criterion_wrapper.hpp"
#include <gmock/gmock.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* tree_by_levels(const struct Tree* tree, size_t* tree_size);
static void print_array(size_t length, const int array[]);
static void print_tree(const Tree* tree);
void do_test(const Tree* tree, size_t exp_len, const int expected[]);

Test(tests_suite, sample_tests) {
    Tree node4 = {.value = 4};
    Tree node5 = {.value = 5};
    Tree node6 = {.value = 6};
    Tree node8 = {.value = 8};
    Tree node7 = {.left = &node8, .value = 7};
    Tree node2 = {.left = &node4, .right = &node5, .value = 2};
    Tree node3 = {.left = &node6, .right = &node7, .value = 3};
    Tree tree = {.left = &node2, .right = &node3, .value = 1};

    do_test(&tree, 8, (const int[8]){1, 2, 3, 4, 5, 6, 7, 8});
    do_test(NULL, 0, NULL);
}

/* ==================================================================================== */
/* ==========================  PRINTING FUNCTIONS  ==================================== */
/* ==================================================================================== */

static void print_tree_rec(const Tree* tree, int depth) {
    if (tree == NULL) return;

    for (int i = 0; i < depth; i++) printf("----");
    printf("%d\n", tree->value);

    print_tree_rec(tree->left, depth + 1);
    print_tree_rec(tree->right, depth + 1);
}

static void print_tree(const Tree* tree) {
    if (tree == NULL)
        printf("NULL\n");
    else
        print_tree_rec(tree, 0);
}

static void print_array(size_t length, const int array[]) {
    if (length == 0) {
        printf("{}\n");
        return;
    }
    printf("{");
    for (size_t i = 0; i < length - 1; i++) printf("%d, ", array[i]);
    printf("%d}\n", array[length - 1]);
}

void do_test(const Tree* tree, size_t exp_len, const int expected[]) {
    size_t act_len = 42;
    int* actual = tree_by_levels(tree, &act_len);

    size_t nb_bytes = exp_len * sizeof *expected;

    if (act_len != exp_len || memcmp(actual, expected, nb_bytes)) {
        puts("for tree:");
        print_tree(tree);
        puts("expected:");
        print_array(exp_len, expected);
        puts("actual:");
        print_array(act_len, actual);
        fflush(stdout);
    }

    cr_assert_eq(act_len, exp_len, "wrong tree size: expected %zu, but got %zu", exp_len, act_len);

    cr_assert_arr_eq(actual, expected, nb_bytes);

    free(actual);
}
