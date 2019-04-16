""" @ symbol is equivalent to calling the decorator on the function it wraps
and assigning the return value to the original name in the same scope
"""
from functools import wraps


def trace_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
            (func.__name__, args, kwargs, result))
        return result
    return wrapper


@trace_one
def fibonacci_one(n):
    """ Return the n-th fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci_one(n - 2) + fibonacci_one(n - 1))


def example_one():
    """
    >>> 
    fibonacci_one((1,), {}) -> 1
    fibonacci_one((0,), {}) -> 0
    fibonacci_one((1,), {}) -> 1
    fibonacci_one((2,), {}) -> 1
    fibonacci_one((3,), {}) -> 2
    """
    fibonacci_one(3)


def example_two():
    """
    >>> 
    <function trace_one.<locals>.wrapper at 0x7f5acf8ce6a8>
    """
    print(fibonacci_one)


def example_three():
    """
    >>> 
    Help on function wrapper in module __main__:
    wrapper(*args, **kwargs)
    """
    help(fibonacci_one)


def trace_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
            (func.__name__, args, kwargs, result))
        return result
    return wrapper


@trace_two
def fibonacci_two(n):
    """ Return the n-th fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci_two(n - 2) + fibonacci_two(n - 1))


def example_four():
    """
    >>> 
    Help on function fibonacci_two in module __main__:
    fibonacci_two(n)
        Return the n-th fibonacci number
    """
    help(fibonacci_two)


def main():
    example_four()


if __name__ == '__main__':
    main()
