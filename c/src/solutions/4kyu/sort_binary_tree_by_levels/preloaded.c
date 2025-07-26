#include <stdio.h>
#include <stdlib.h>

static int news = 0;
static int frees = 0;

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
    Queue* queue = (Queue*)malloc(sizeof *queue);
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

size_t queue_size(const Queue* queue) {
    return queue->size;
}

Queue* queue_enqueue(Queue* queue, const void* data) {
    QueueNode* node = (QueueNode*)malloc(sizeof *node);
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
    if (queue->size == 0) return NULL;

    QueueNode* front = queue->front;
    void* data = (void*)front->data;  // the cast is a necessary evil here
    queue->front = front->next;
    if (queue->size == 1) queue->back = NULL;

    free(front);
    queue->size--;
    return data;
}
