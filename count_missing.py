from collections import defaultdict


def log_missing():
    print('Key added')
    return 0


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


if __name__ == '__main__':
    current = {'green': 12, 'blue': 3}
    increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9),
    ]

    # result, count = increment_with_report(current, increments)
    counter = BetterCountMissing()
    assert callable(counter)

    result = defaultdict(counter, current)
    for key, amount in increments:
        result[key] += 1

    assert counter.added == 2
