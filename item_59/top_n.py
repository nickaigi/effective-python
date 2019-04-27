"""Python 3.4 introduced a new 'tracemalloc' built-in module for solving the
problem with gc.get_objects
    - see module notes on using_gc.py
"""


import tracemalloc
import waste_memory


def example_one():
    """
    /path/to/waste_memory.py:7: size=2392 KiB (+2392 KiB), count=29987 (+29987), average=82 B
    /path/to/waste_memory.py:8: size=869 KiB (+869 KiB), count=10000 (+10000), average=89 B
    /path/to/waste_memory.py:14: size=547 KiB (+547 KiB), count=10000 (+10000), average=56 B
    """
    tracemalloc.start(10)  # Save upto 10 stack frames

    time1 = tracemalloc.take_snapshot()
    x = waste_memory.run()
    time2 = tracemalloc.take_snapshot()

    stats = time2.compare_to(time1, 'lineno')
    for stat in stats[:3]:
        print(stat)


def main():
    example_one()


if __name__ == '__main__':
    main()
