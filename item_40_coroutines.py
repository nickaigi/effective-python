from collections import namedtuple


ALIVE = '*'
EMPTY = '-'


Query = namedtuple('Query', ('y', 'x'))


def my_coroutine():
    while True:
        received = yield
        print('Received: ', received)


def example_one():
    """
    >>> 
    Received:  First
    Received:  Second

    The initial next is required to prepare the generator for receiving the
    first send by advancing it to the first yield expression
    """
    it = my_coroutine()
    next(it)           # Prime the coroutine
    it.send('First')
    it.send('Second')


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

def example_two():
    """
    >>> 
    10
    4
    4
    -1

    """
    it = minimize()
    next(it)           # Prime the generator
    print(it.send(10))
    print(it.send(4))
    print(it.send(22))
    print(it.send(-1))



def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # NorthEast

    e_ = yield Query(y + 0, x + 1)  # East
    se = yield Query(y - 1, x + 1)  # SouthEast

    s_ = yield Query(y - 1, x + 0)  # South
    sw = yield Query(y - 1, x - 1)  # SouthWest

    w_ = yield Query(y + 0, x - 1)  # West
    nw = yield Query(y + 1, x - 1)  # NorthWest

    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


def example_three():
    """
    >>> 
    First yield:  Query(y=11, x=5)
    Second yield:  Query(y=11, x=6)
    ...
    Count:  2
    """
    it = count_neighbors(10, 5)
    q1 = next(it)                # Get the first query
    print('First yield: ', q1)
    q2 = it.send(ALIVE)          # Send q1 state, get q2
    print('Second yield: ', q2)
    q3 = it.send(ALIVE)          # Send q2 state, get q3
    print('...')
    q4 = it.send(EMPTY)
    q5 = it.send(EMPTY)
    q6 = it.send(EMPTY)
    q7 = it.send(EMPTY)
    q8 = it.send(EMPTY)
    try:
        it.send(EMPTY)         # Send q8 state, retrieve count
    except StopIteration as e:
        print('Count: ', e.value)  # value form return statement


def main():
    example_three()


if __name__ == '__main__':
    main()
