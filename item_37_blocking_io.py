import select
from time import time
from threading import Thread


def slow_systemcall():
    # select.select([socket.socket()], [], [], 0.1)
    select.select([], [], [], 0.1)


def example_three():
    """
    >>> 
    Took 0.501 seconds
    """
    start = time()
    for _ in range(5):
        slow_systemcall()
    end = time()
    print('Took %.3f seconds' % (end - start))


def compute_helicopter_location(index):
    pass


def example_four():
    """
    >>> 
    Took 0.101 seconds
    """
    start = time()
    threads = []
    for _ in range(5):
        thread = Thread(target=slow_systemcall)
        thread.start()
        threads.append(thread)

    for i in range(5):
        compute_helicopter_location(i)
    for thread in threads:
        thread.join()
    end = time()
    print('Took %.3f seconds' % (end - start))


def main():
    example_four()


if __name__ == '__main__':
    main()
