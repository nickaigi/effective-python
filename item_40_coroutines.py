from collections import namedtuple


ALIVE = '*'
EMPTY = '-'
Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))
TICK = object()


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


def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate
    return state


def example_four():
    """
    >>> 
    Me:       Query(y=10, x=5)
    Q1:       Query(y=11, x=5)
    ...
    Outcome:  Transition(y=10, x=5, state='-')
    """
    it = step_cell(10, 5)
    q0 = next(it)            # Initial location query
    print('Me:      ', q0)
    q1 = it.send(ALIVE)      # Send my status, get neighbor query
    print('Q1:      ', q1)
    print('...')
    q2 = it.send(ALIVE)
    q3 = it.send(ALIVE)
    q4 = it.send(ALIVE)
    q5 = it.send(ALIVE)
    q6 = it.send(EMPTY)
    q7 = it.send(EMPTY)
    q8 = it.send(EMPTY)
    t1 = it.send(EMPTY)    # Send for q8, get same decision
    print('Outcome: ', t1)


def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x):
        self.rows[y % self.height][x % self.width] = state


def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:  # must be a transition
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)


def example_five():
    grid = Grid(5, 9)
    grid.assign(0, 3, ALIVE)
    grid.assign(1, 4, ALIVE)
    grid.assign(2, 2, ALIVE)
    grid.assign(2, 3, ALIVE)
    grid.assign(2, 4, ALIVE)
    print(grid)


class ColumnPrinter(object):
    def __init__(self):
        self.columns = []

    def append(self, data):
        self.columns.append(data)

    def __str__(self):
        row_count = 1
        for data in self.columns:
            row_count = max(row_count, len(data.splitlines()) + 1)
        rows = [''] * row_count
        for j in range(row_count):
            for i, data in enumerate(self.columns):
                line = data.splitlines()[max(0, j - 1)]
                if j == 0:
                    padding = ' ' * (len(line) // 2)
                    rows[j] += padding + str(i) + padding
                else:
                    rows[j] += line
                if (i + 1) < len(self.columns):
                    rows[j] += ' | '
        return '\n'.join(rows)

columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)
for i in range(5):
    columns.append(str(grid))
    grid = live_a_generation(grid, sim)


print(columns)


grid = Grid(5,5)
grid.assign(1, 1, ALIVE)
grid.assign(2, 2, ALIVE)
grid.assign(2, 3, ALIVE)
grid.assign(3, 3, ALIVE)


columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)
for i in range(5):
    columns.append(str(grid))
    grid = live_a_generation(grid, sim)


print(columns)


def main():
    example_four()


if __name__ == '__main__':
    main()
