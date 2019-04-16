import logging
from threading import Lock


def example_one():
    lock = Lock()
    with lock:
        print('Lock is held')


def example_two():
    """ equivalent to example_one
    - the with statement is better because it eliminates the need to write
      the repetitive code of the try/finally construction.
    """
    lock = Lock()
    lock.acquire()
    try:
        print('Lock is held')
    finally:
        lock.release()


def main():
    example_two()


if __name__ == '__main__':
    main()
