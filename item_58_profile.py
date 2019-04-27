"""How to profile your code: ignore your intuition, directly measure the
perfomance

Python provides two built-in profilers, one that is pure python 'profile'
and another that is a C-extension module 'cProfile'

cProfile is better because of its minimal impact on the performance of your
program whilte it's being profiled.

'profile' imposes a high overhead that will skew the results


Meaning of profiler statistics columns:
    - ncalls: number of calls to the function during the profiling period.

    - tottime: number of seconds spent executing the funciton, excluding time spent executing other function it calls.

    - tottime percall: average number of seconds spent in the function each
      time it was called, excluding time spent executing other functions it
      calls. This is 'tottime' divided by 'ncalls'.

    - cumtime: cumulative number of seconds spent in the function each time it
      was called, excluding time spent executing other functions it calls.
      This is 'tottime' divided by 'ncalls'.

    -cumtime percall: average number of seconds spent in the function each time
     it was called, including time spent in all other functions it calls.
     This is 'cumtime' divided by 'ncalls'
"""


from random import randint
from cProfile import Profile
from pstats import Stats


def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            # 'L.insert(index, object) -- insert object before index'
            array.insert(i, value)
            return
    array.append(value)


def example_one():
    """
             20003 function calls in 0.778 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.778    0.778 item_58_profile.py:38(<lambda>)
        1    0.001    0.001    0.778    0.778 item_58_profile.py:19(insertion_sort)
    10000    0.764    0.000    0.777    0.000 item_58_profile.py:26(insert_value)
     9989    0.013    0.000    0.013    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

    """
    max_size = 10**4
    data = [randint(0, max_size) for _ in range(max_size)]
    test = lambda: insertion_sort(data)

    profiler = Profile()
    profiler.runcall(test)

    # to extract statistics about the 'test' function's performance, we use pstats
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()


def main():
    example_one()


if __name__ == '__main__':
    main()
