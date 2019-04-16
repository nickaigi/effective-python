import logging
from threading import Lock
from contextlib import contextmanager
logging.getLogger(__name__).setLevel(logging.WARNING)


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


def my_function():
    """
    >>> 
    ERROR:root:Error here
    """
    logging.debug('debug data')
    logging.error('Error here')
    logging.debug('more debug')


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
       yield 
    finally:
        logger.setLevel(old_level)


def example_three():
    """
    >>> 
    inside:
    DEBUG:root:debug data
    ERROR:root:Error here
    DEBUG:root:more debug
    after :
    ERROR:root:Error here
    """
    with debug_logging(logging.DEBUG):
        print('inside: ')
        my_function()
    print('after :')
    my_function()


def main():
    example_three()


if __name__ == '__main__':
    main()
