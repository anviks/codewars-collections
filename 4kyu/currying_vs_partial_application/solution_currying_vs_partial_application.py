"""https://www.codewars.com/kata/currying-vs-partial-application"""

from types import FunctionType


def curry_partial(f, *initial_args):
    """Curries and partially applies the initial arguments to the function."""
    if not isinstance(f, FunctionType):
        return f

    if f.__code__.co_argcount <= len(initial_args):
        return f(*(initial_args[:f.__code__.co_argcount] or initial_args))

    return lambda *args: curry_partial(f, *initial_args, *args)
