/*
 * https://www.codewars.com/kata/5c0c5ec84e8f1804b9000296
 */

#include "solution_ordered_set.h"

#include <stdlib.h>
#include <string.h>

typedef int (*Comparator)(const void*, const void*);

typedef char* (*Stringizer)(const void*);

typedef struct {
    void* value;
    struct Node* left;
    struct Node* right;
} Node;

struct Set {
    Node* root;
    size_t size;
    size_t capacity;

    Comparator comparator;
    Stringizer stringizer;
};

Node* create_node(void* value) {
    Node* node = malloc(sizeof(Node));
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// unsigned int get_insertion_index(const Set* set, const void* item) {
//     if (set->size == 0) {
//         return 0;
//     }
//
//     unsigned int low = 0, high = set->size - 1;
//
//     while (low <= high) {
//         const unsigned int mid = low + (high - low) / 2;
//         const int comparison = set->comparator(set->stuff[mid], item);
//
//         if (comparison == 0) {
//             return mid;
//         }
//
//         if (comparison < 0) {
//             low = mid + 1;
//         } else {
//             if (mid == 0) return low;
//             high = mid - 1;
//         }
//     }
//
//     return low;
// }

Set* set_initialize(Comparator comparator, Stringizer stringizer) {
    Set* set = malloc(sizeof(Set));

    set->size = 0;
    set->capacity = 100;
    set->root = NULL;
    set->comparator = comparator;
    set->stringizer = stringizer;

    return set;
}

void bst_destroy(Node* root) {
    if (!root)
        return;
    bst_destroy(root->left);
    bst_destroy(root->right);
    free(root);
}

void set_destroy(Set* set) {
    bst_destroy(set->root);
    free(set);
}

size_t set_size(const Set* set) { return set->size; }

int bst_search(Node* root, void* value, Comparator cmp) {
    if (!root)
        return 0;

    int c = cmp(value, root->value);
    if (c == 0)
        return 1;
    if (c < 0)
        return bst_search(root->left, value, cmp);
    return bst_search(root->right, value, cmp);
}

int set_includes(const Set* set, const void* value) { return bst_search(set->root, value, set->comparator); }

// void check_capacity(Set* set) {
//     if (set->size == set->capacity) {
//         set->capacity += 100;
//     } else if (set->capacity - set->size >= 200) {
//         set->capacity -= 100;
//     } else {
//         return;
//     }
//     void** newStuff = realloc(set->stuff, set->capacity * sizeof(void*));
//     if (!newStuff) {
//         exit(EXIT_FAILURE);
//     }
//     set->stuff = newStuff;
// }

Node* bst_insert(Node* root, void* value, Comparator cmp) {
    if (root == NULL)
        return create_node(value);

    int c = cmp(value, root->value);
    if (c < 0)
        root->left = bst_insert(root->left, value, cmp);
    else if (c > 0)
        root->right = bst_insert(root->right, value, cmp);
    // if equal, do nothing (set: no duplicates)

    return root;
}

void set_insert(Set* set, void* value) { set->root = bst_insert(set->root, value, set->comparator); }

Node* bst_remove(Node* root, void* value, Comparator cmp) {
    if (!root)
        return NULL;

    int comp = cmp(value, root->value);
    if (comp < 0) {
        root->left = bst_remove(root->left, value, cmp);
    } else if (comp > 0) {
        root->right = bst_remove(root->right, value, cmp);
    } else {
        // Case 1: no children
        if (!root->left && !root->right) {
            free(root);
            return NULL;
        }
        // Case 2: one child
        else if (!root->left || !root->right) {
            Node* child = root->left ? root->left : root->right;
            free(root);
            return child;
        }
        // Case 3: two children
        else {
            // Find in-order successor (leftmost node in right subtree)
            Node* successor = root->right;
            while (successor->left) {
                successor = successor->left;
            }

            root->value = successor->value;
            // Recursively delete the successor
            root->right = bst_remove(root->right, successor->value, cmp);
        }
    }

    return root;
}

void set_remove(Set* set, void* value) { set->root = bst_remove(set->root, value, set->comparator); }
