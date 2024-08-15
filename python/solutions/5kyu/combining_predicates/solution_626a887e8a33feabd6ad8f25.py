"""https://www.codewars.com/kata/626a887e8a33feabd6ad8f25"""

from functools import update_wrapper
from typing import Callable

_P = Callable[..., bool]


class predicate:
    def __init__(self, func: _P):
        self.func = func
        update_wrapper(self, func)

    def __and__(self, other: _P) -> 'predicate':
        return predicate(lambda *args, **kwargs: self.func(*args, **kwargs) and other(*args, **kwargs))

    def __or__(self, other: _P) -> 'predicate':
        return predicate(lambda *args, **kwargs: self.func(*args, **kwargs) or other(*args, **kwargs))

    def __invert__(self) -> 'predicate':
        return predicate(lambda *args, **kwargs: not self.func(*args, **kwargs))

    def __call__(self, *args, **kwargs) -> bool:
        return self.func(*args, **kwargs)
