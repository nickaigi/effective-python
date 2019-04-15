from time import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


numbers = [
    (1963309, 2265973), (2030677, 3814172), (1551645, 2229620),
    (2039045, 2020802)
]


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def example_one():
    """
    >>> 
    Took 0.282 seconds
    """
    start = time()
    results = list(map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))


def example_two():
    """
    not particularly faster than example_one
    - overhead of starting and communicating with the pool of threads
    >>> 
    Took 0.279 seconds
    """
    start = time()
    # max_workers: match the number of cpu cores on your computer
    pool = ThreadPoolExecutor(max_workers=4)
    results = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))


def example_three():
    """
    change to ProcessPoolExecutor
    >>> 
    Took 0.100 seconds
    """
    start = time()
    pool = ProcessPoolExecutor(max_workers=4)  # only change
    results = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))


def main():
    example_three()


if __name__ == '__main__':
    main()
