#ifndef CODEWARS_C_SOLUTION_ORDERED_SET_H
#define CODEWARS_C_SOLUTION_ORDERED_SET_H

#ifdef __cplusplus
extern "C" {
#endif
#include <stddef.h>

    typedef int (*Comparator)(const void *, const void *);
    typedef char *(*Stringizer)(const void *);

    typedef struct Set Set;

    Set *set_initialize(Comparator, Stringizer);
    void set_destroy(Set *);
    size_t set_size(const Set *);
    int set_includes(const Set *, const void *);
    void set_insert(Set *, const void *);
    void set_remove(Set *, const void *);
    
#ifdef __cplusplus
}
#endif

#endif //CODEWARS_C_SOLUTION_ORDERED_SET_H