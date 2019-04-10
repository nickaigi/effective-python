def my_coroutine():
    while True:
        received = yield
        print('Received: ', received)


def example_one():
    """
    The initial next is required to prepare the generator for receiving the
    first send by advancing it to the first yield expression
    """
    it = my_coroutine()
    next(it)
    it.send('First')
    it.send('Second')


def main():
    example_one()


if __name__ == '__main__':
    main()
