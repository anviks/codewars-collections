from types import FunctionType


def curry_partial(f, *initial_args):
    """Curries and partially applies the initial arguments to the function."""
    if not isinstance(f, FunctionType):
        return f

    if f.__code__.co_argcount <= len(initial_args):
        return f(*(initial_args[:f.__code__.co_argcount] or initial_args))

    return lambda *args: curry_partial(f, *initial_args, *args)


def add(x, y, z):
    return x + y + z


if __name__ == '__main__':
    curried_add = curry_partial(add)
    print(curried_add(1)(2)(3))  # => 6

    partial_add = curry_partial(add, 1)
    print(partial_add(2, 3))  # => 6

    curry_partial(add)(1)(2)(3)  # =>6
    curry_partial(add, 1)(2)(3)  # =>6
    curry_partial(add, 1)(2, 3)  # =>6
    curry_partial(add, 1, 2)(3)  # =>6
    curry_partial(add, 1, 2, 3)  # =>6
    curry_partial(add)(1, 2, 3)  # =>6
    curry_partial(add)(1, 2)(3)  # =>6
    curry_partial(add)()(1, 2, 3)  # =>6
    curry_partial(add)()(1)()()(2)(3)  # =>6

    curry_partial(add)()(1)()()(2)(3, 4, 5, 6)  # =>6
    curry_partial(add, 1)(2, 3, 4, 5)  # =>6

    print(curry_partial(curry_partial(curry_partial(add, 1), 2), 3))  # =>6
    print(curry_partial(curry_partial(add, 1, 2), 3))  # =>6
    print(curry_partial(curry_partial(add, 1), 2, 3))  # =>6
    print(curry_partial(curry_partial(add, 1), 2)(3))  # =>6
    print(curry_partial(curry_partial(add, 1)(2), 3))  # =>6
    print(curry_partial(curry_partial(curry_partial(add, 1)), 2, 3))  # =>6
