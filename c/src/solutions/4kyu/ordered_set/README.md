# [Ordered set](https://www.codewars.com/kata/5c0c5ec84e8f1804b9000296)

# Task

Implement a `set` data structure similar to the `std::set` found in C++.

The key features of `std::set`:

* Generic
* Contains only unique elements
* Elements are stored in a sorted order

**Note**: the ordering of the elements will not be tested, but your implementation must support fast lookup/insertion/deletion, and keeping the elements sorted is the easier way to achieve this.

The `set` can be implemented however you want, but the following operations must be supported:

```c
Set *set_initialize(Comparator, Stringizer)       // initialize a set
void set_destroy(Set *)                           // destroy the set
size_t set_size(const Set *)                      // get the number of elements
int set_includes(const Set *, const void *)       // check the element's presence
void set_insert(Set *, const void *)              // add an element
void set_remove(Set *, const void *)              // remove an element
```

All the declarations above should be self-explanatory. The only exception is `set_initialize` which receives 2 special arguments:
* `Comparator` - a function which takes 2 values, and returns zero if they are equal, or a negative/positive number if the first argument is less/greater than the second, respectively
* `Stringizer` - a function which returns the stringified representation of the element