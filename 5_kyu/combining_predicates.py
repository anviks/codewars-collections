from functools import update_wrapper
from typing import Callable

_P = Callable[..., bool]


class predicate:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __and__(self, other):
        return predicate(lambda *args, **kwargs: self.func(*args, **kwargs) and other(*args, **kwargs))

    def __or__(self, other):
        return predicate(lambda *args, **kwargs: self.func(*args, **kwargs) or other(*args, **kwargs))

    def __invert__(self):
        return predicate(lambda *args, **kwargs: not self.func(*args, **kwargs))

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@predicate
def is_even(num):
    return num % 2 == 0


@predicate
def is_positive(num):
    return num > 0


print((is_even & is_positive)(4))  # True
print((is_even & is_positive)(3))  # False
print((is_even | is_positive)(3))  # True
print((~is_even & is_positive)(3))  # True


@predicate
def to_be():
    return True


print((to_be | ~to_be)())  # True


@predicate
def is_equal(a, b):
    return a == b


@predicate
def is_less_than(a, b):
    return a < b


print((is_less_than | is_equal)(1, 2))  # True
print((is_less_than | is_equal)(2, b=2))  # True
print((is_less_than | is_equal)(a=3, b=2))  # False


@predicate
def is_less_than(a, b):
    return a < b


print(is_less_than(1, 2))  # True
print(is_less_than(2, 2))  # False
print(is_less_than(3, 2))  # False
