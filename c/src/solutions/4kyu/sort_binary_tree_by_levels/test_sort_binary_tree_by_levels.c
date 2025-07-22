/*
 * https://www.codewars.com/kata/52bef5e3588c56132c0003bc
 */

#include "solution_sort_binary_tree_by_levels.h"

#include <criterion/criterion.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int news = 0;
static int frees = 0;

int* tree_by_levels(const struct Tree* tree, size_t* tree_size);
static void print_array(size_t length, const int array[length]);
static void print_tree(const Tree* tree);
void do_test (const Tree *tree, size_t exp_len, const int expected[exp_len]);

Test(tests_suite, sample_tests)
{
	Tree *tree = &(Tree)
	{
		.value = 1,
		.left = &(Tree)
		{
			.value = 2,
			.left = &(Tree) { .value = 4 },
			.right = &(Tree) { .value = 5 },
		},
		.right = &(Tree)
		{
			.value = 3,
			.left = &(Tree){.value = 6},
			.right = &(Tree)
			{
				.value = 7,
				.left = &(Tree) { .value = 8 }
			}
		}
	};
	do_test(tree, 8, (const int[8]){1, 2, 3, 4, 5, 6, 7, 8});
	do_test(NULL, 0, NULL);
}

/* =============================================================================== */
/* ==========================   PRELOADED STUFF   ================================ */
/* =============================================================================== */

void do_test(const Tree* tree, size_t exp_len, const int expected[exp_len]) {
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

    cr_assert_arr_eq(actual, expected, nb_bytes, "incorrect array");

    if (news != frees)
        cr_assert_fail("if you create a queue you must free it afterwards !");

    free(actual);
}

/* ==================================================================================== */
/* ==========================  PRINTING FUNCTIONS  ==================================== */
/* ==================================================================================== */

static void print_tree_rec(const Tree* tree, int depth) {
    if (tree == NULL)
        return;

    for (int i = 0; i < depth; i++)
        printf("----");
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

static void print_array(size_t length, const int array[length]) {
    if (length == 0) {
        printf("{}\n");
        return;
    }
    printf("{");
    for (size_t i = 0; i < length - 1; i++)
        printf("%d, ", array[i]);
    printf("%d}\n", array[length - 1]);
}

/* ==================================================================================== */
/* ==========================   QUEUE IMPLEMENTATION   ================================ */
/* ==================================================================================== */

typedef struct QueueNode {
    const void* data;
    struct QueueNode *previous, *next;
} QueueNode;

typedef struct Queue {
    struct QueueNode *front, *back;
    size_t size;
} Queue;

Queue* new_queue(void) {
    news++;
    Queue* queue = malloc(sizeof *queue);
    queue->front = queue->back = NULL;
    queue->size = 0;
    return queue;
}

void free_queue(Queue* queue) {
    frees++;
    for (QueueNode* node = queue->front; node != NULL;) {
        QueueNode* next = node->next;
        free(node);
        node = next;
    }
    free(queue);
}

size_t queue_size(const Queue* queue) { return queue->size; }

Queue* queue_enqueue(Queue* queue, const void* data) {
    QueueNode* node = malloc(sizeof *node);
    node->data = data;
    node->next = NULL;
    node->previous = queue->back;

    if (queue->size == 0)
        queue->front = node;
    else
        queue->back->next = node;

    queue->back = node;
    queue->size++;
    return queue;
}

void* queue_dequeue(Queue* queue) {
    if (queue->size == 0)
        return NULL;

    QueueNode* front = queue->front;
    void* data = (void*)front->data;  // the cast is a necessary evil here
    queue->front = front->next;
    if (queue->size == 1)
        queue->back = NULL;

    free(front);
    queue->size--;
    return data;
}
