def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
