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


def example_four():
    """the context manager passed to a 'with' statement may also return an
    object
    - this approach is preferable to manually opening and closing the file
      handle every time. It gives you confidence that the file is eventually
      closed when execution leaves the 'with' statement.
    - Its good practice to reduce the amount of code that executes while the
      file handle is open
    """
    with open('/tmp/my_file.txt', 'w') as handle:
        handle.write('This is some data!')


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


def example_five():
    """
    I don't get any output on this code
    """
    with log_level(logging.DEBUG, 'my-log') as logger:
        logger.debug('This is my message!')
        logging.debug('This will not print')


def example_six():
    """
    >>> 
    Error will print
    """
    logger = logging.getLogger('my-log')
    logger.debug('Debug will not print')
    logger.error('Error will print')


def main():
    example_six()


if __name__ == '__main__':
    main()
