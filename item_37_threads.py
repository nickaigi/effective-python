from time import time
from threading import Thread


numbers = [2139079, 1214759, 1516637, 1852285]


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


def example_one():
    """
    Running factorize in serial

    >>> 
    Took 0.238 seconds
    """
    start = time()
    for number in numbers:
        list(factorize(number))
    end = time()
    print('Took %.3f seconds' % (end - start))


def example_two():
    """
    - Running factorize in parallel
    - what's surprising is that this takes even longer.

    >>> 
    Took 0.246 seconds
    """
    start = time()
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end = time()
    print('Took %.3f seconds' % (end - start))


def main():
    example_two()


if __name__ == '__main__':
    main()
