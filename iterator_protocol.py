# demonstrates a class that implements the iterator protocol


class ReadVisits(object):
    """ when python sees a statement like below, it will call iter(foo)

        for x in foo

    - the iter built-in function calls the foo.__iter__ special method in turn
    - the __iter__ method must return an iterator object
      (which itself implements the __next__ special method)
    - then the for loop repeatedly calls the next built-in function.
    """
    def __init__(self, data_list):
        self.data_list = data_list

    def __iter__(self):
        for rec in self.data_list:
            yield rec


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


if __name__ == '__main__':
    visits = ReadVisits([15, 35, 80])
    percentages = normalize(visits)
    print(percentages)
