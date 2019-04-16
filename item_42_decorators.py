""" @ symbol is equivalent to calling the decorator on the function it wraps
and assigning the return value to the original name in the same scope
"""


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
            (func.__name__, args, kwargs, result))
        return result
    return wrapper


@trace
def fibonacci(n):
    """ Return the n-th fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


def example_one():
    """
    >>> 
    fibonacci((1,), {}) -> 1
    fibonacci((0,), {}) -> 0
    fibonacci((1,), {}) -> 1
    fibonacci((2,), {}) -> 1
    fibonacci((3,), {}) -> 2
    """
    fibonacci(3)


def main():
    example_one()


if __name__ == '__main__':
    main()
