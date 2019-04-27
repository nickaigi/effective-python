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
from bisect import bisect_left


def insertion_sort(data):
    result = []
    for value in data:
        # insert_value(result, value)
        insert_value_better(result, value)
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


    - notes for Nick:
        - we can see that the biggest use of CPU in our test is the cumulative
          time spent in the 'insert_value' function.
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


def insert_value_better(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)


def example_two():
    """
             30003 function calls in 0.018 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 item_58_profile.py:98(<lambda>)
        1    0.001    0.001    0.018    0.018 item_58_profile.py:38(insertion_sort)
    10000    0.002    0.000    0.017    0.000 item_58_profile.py:88(insert_value_better)
    10000    0.012    0.000    0.012    0.000 {method 'insert' of 'list' objects}
    10000    0.003    0.000    0.003    0.000 {built-in method _bisect.bisect_left}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



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


def my_utility(a, b):
    c = 1
    for i in range(100):
        c += a * b


def first_func():
    for _ in range(1000):
        my_utility(4, 5)


def second_func():
    for _ in range(10):
        my_utility(1, 3)


def my_program():
    for _ in range(20):
        first_func()
        second_func()


def example_three():
    """
             20242 function calls in 0.063 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.063    0.063 item_58_profile.py:140(my_program)
       20    0.002    0.000    0.063    0.003 item_58_profile.py:130(first_func)
    20200    0.061    0.000    0.061    0.000 item_58_profile.py:124(my_utility)
       20    0.000    0.000    0.001    0.000 item_58_profile.py:135(second_func)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



    -notes for Nick
        - you may profile your program only to find that a common utility
          function is responsible for majority of the execution time.

        - default output from the profiler doesn't show how the utility
          function is called by many different parts of your program.

        - 'my_utility' function is evidently the source of most execution time,
          but it is not immediately obvious why that function is called so many times.

    ---- Callers -----

    Ordered by: cumulative time

    Function                                          was called by...
                                                          ncalls  tottime  cumtime
    item_58_profile.py:140(my_program)                <-
    item_58_profile.py:130(first_func)                <-      20    0.002    0.062  item_58_profile.py:140(my_program)
    item_58_profile.py:124(my_utility)                <-   20000    0.061    0.061  item_58_profile.py:130(first_func)
                                                             200    0.001    0.001  item_58_profile.py:135(second_func)
    item_58_profile.py:135(second_func)               <-      20    0.000    0.001  item_58_profile.py:140(my_program)
    {method 'disable' of '_lsprof.Profiler' objects}  <-



    """
    profiler = Profile()
    profiler.runcall(my_program)

    # to extract statistics about the 'test' function's performance, we use pstats
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()

    print('\n---- Callers -----\n')

    # to see how many times a function is called
    stats.print_callers()




def main():
    example_three()


if __name__ == '__main__':
    main()
