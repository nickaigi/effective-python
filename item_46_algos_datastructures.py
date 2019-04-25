from collections import deque, OrderedDict, defaultdict
from random import randint
import heapq
from bisect import bisect_left


def example_one():
    """
    deque
        - double ended queue.
        - provides constant time - O(1) - operations for inserting or removing items
          from its beginning or end
        - TODO: compare with a list
            - insertion and removal from end of the list takes constant time.
            - inserting or removing from head of a list takes
              linear time - O(n) - (depend on n - number of items in the list)
              which is much slower that the constant time of a deque
    """
    fifo = deque()
    fifo.append(1)      # Producer
    x = fifo.popleft()  # Consumer


def example_two():
    """
    Ordered Dictionary

    results in an infinite loop
    """
    a = {}
    a['foo'] = 1
    a['bar'] = 2

    # Randomly populate 'b' to cause hash conflicts
    # Infinite Loop
    while True:
        z = randint(99, 1013)
        b = {}
        for i in range(z):
            b[i] = i
        b['foo'] = 1
        b['bar'] = 2
        for i in range(z):
            del b[i]
        if str(b) != str(a):
            break
    print(a)
    print(b)
    print('Equal?', a == b)


def example_three():
    """
    >>> 
    1 red
    2 blue
    """
    a = OrderedDict()
    a['foo'] = 1
    a['bar'] = 2

    b = OrderedDict()
    b['foo'] = 'red'
    b['bar'] = 'blue'

    for value1, value2 in zip(a.values(), b.values()):
        print(value1, value2)


def example_five():
    """
    dict
        - you have to check for the existance of a key before accessing the value
    """
    stats = {}
    key = 'my_customer'
    if key not in stats:
        stats[key] = 0
    stats[key] += 1


def example_six():
    """
    defaultdict
        - automatically stores a default value when a key doesn't exist.
        - you have to provide a function that will return the default value
          each time a key is missing.
    """
    stats = defaultdict(int)
    stats['my_counter'] += 1


def example_seven():
    """
    Heap Queue
        - heaps are useful for maintaining priority queues.
        - insertion by any order.
        - removal by highest priority (lowest number)
    >>> 
    3 4 5 7
    """
    a = []
    heapq.heappush(a, 5)
    heapq.heappush(a, 3)
    heapq.heappush(a, 7)
    heapq.heappush(a, 4)

    print(heapq.heappop(a), heapq.heappop(a), heapq.heappop(a), heapq.heappop(a))


def example_eight():
    """
    heapq operations take logarithmic time O(log(n)) where n is the size of the list
    - same operations using a python list is O(n) linear time
    >>> 
    Before: [3, 4, 7, 5]
    After:  [3, 4, 5, 7]
    """
    a = []
    heapq.heappush(a, 5)
    heapq.heappush(a, 3)
    heapq.heappush(a, 7)
    heapq.heappush(a, 4)

    assert a[0] == heapq.nsmallest(1, a)[0] == 3

    print('Before:', a)
    a.sort()
    print('After: ', a)


def example_nine():
    """
    Searching in a list takes linear time O(n)
    """
    x = list(range(10**6))
    i = x.index(991234)


def example_ten():
    """
    bisect_left
        - provides binary search through a sequence of sorted items
        - returns an index, the insertion point of the value in the seq
        - binary search is is O(log(n)) logarithmic, using bisect to search a
          list of 1M takes roughly the same amount of time as index to linearly
          search a list of 14 items.  blazing fast

    """
    x = list(range(10**6))
    i = bisect_left(x, 991234)


def main():
    example_ten()


if __name__ == '__main__':
    main()
