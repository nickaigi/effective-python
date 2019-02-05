# demonstrates how to get data out of a closure
# on way is to use nonlocal keyword
# nonlocal Py3 only, makes it clear when data is being assigned out of a
# closure into another scope. CAUTION


def sort_priority(numbers, group):
    """ Python scope is determined by LEGB
        - local
        - enclosing
        - global
        - built-in scope
    """
    found = False

    def helper(x):
        nonlocal found  # assert that we want to refer to the enclosing scope
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

# it is better to wrap your state in a helper class


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}

    # nonlocal style
    # found = sort_priority(numbers, group)
    # print('Found: ', found)
    # print(numbers)

    # helper class style

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert sorter.found is True
