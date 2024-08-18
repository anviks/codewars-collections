# [Combining predicates](https://www.codewars.com/kata/626a887e8a33feabd6ad8f25)

# Task

Create a decorator `@predicate` which allows boolean functions to be conveniently combined using `&`, `|` and `~` operators:

```python
@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0

(is_even & is_positive)(4)   # True
(is_even & is_positive)(3)   # False
(is_even | is_positive)(3)   # True
(~is_even & is_positive)(3)  # True
```

It should work with all functions, regardless of how many arguments they accept:

```python
@predicate
def to_be():
    return True

(to_be | ~to_be)()  # True

@predicate
def is_equal(a, b):
    return a == b

@predicate
def is_less_than(a, b):
    return a < b

(is_less_than | is_equal)(1, 2)      # True
```

Keyword arguments should work as well:

```python
(is_less_than | is_equal)(2, b=2)    # True
(is_less_than | is_equal)(a=3, b=2)  # False
```

Combinations of functions with incompatible signatures (e.g. `is_positive & is_less_than`) will not be tested.

A decorated function should be callable by itself (without combining with other predicates) and behave like the original function:

```python
@predicate
def is_less_than(a, b):
    return a < b

is_less_than(1, 2)  # True
is_less_than(2, 2)  # False
is_less_than(3, 2)  # False
```

Good luck!

This kata is heavily inspired by [FArekkusu](https://www.codewars.com/users/FArekkusu)'s [Readable Specification Pattern](https://www.codewars.com/kata/5dc424122c135e001499d0e5), but should be a bit easier. You should try his kata as well!