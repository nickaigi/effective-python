from collections import deque, OrderedDict
from random import randint

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
        #z = randint(99, 1013)
        z = randint(1, 20)
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


def main():
    example_two()


if __name__ == '__main__':
    main()
