from collections import deque

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
    """
def main():
    example_one()

if __name__ == '__main__':
    main()
