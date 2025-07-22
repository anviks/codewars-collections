/*
 * https://www.codewars.com/kata/52bef5e3588c56132c0003bc
 */

#include "solution_sort_binary_tree_by_levels.h"

#include <stddef.h>
#include <stdlib.h>

/* to help you solve the kata, a queue implementation has been
preloaded for you */

typedef struct Queue Queue;

// the queue elements are pointers

// creates a new queue
extern Queue* new_queue(void);
// returns the number of elements in the queue
extern size_t queue_size(const Queue* queue);
// adds an element at the back of the queue and returns the queue
extern Queue* queue_enqueue(Queue* queue, const void* data);
// removes the element at the front of the queue and returns it
extern void* queue_dequeue(Queue* queue);
// frees the queue, do not forget to call it !
extern void free_queue(Queue* queue);
/* ==================================================== */

int* tree_by_levels(const Tree* tree, size_t* tree_size) {
    *tree_size = 0;
    if (!tree) return NULL;

    int result_size = 20;
    int* result = malloc(result_size * sizeof(int));
    
    Queue* queue = new_queue();
    queue_enqueue(queue, tree);

    while (queue_size(queue) > 0) {
        Tree* node = queue_dequeue(queue);
        if (!node) continue;

        if (*tree_size >= result_size) {
            result_size += 20;
            result = realloc(result, result_size * sizeof(int));
        }

        result[(*tree_size)++] = node->value;

        queue_enqueue(queue, node->left);
        queue_enqueue(queue, node->right);
    }

    free_queue(queue);
    
    return result;
}
