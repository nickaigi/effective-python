# this code demonstrates how to use a generator in a scenario where
# I would have returned a list


def get_even_numbers(nums):
    """the traditional way is to return a list"""
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result


def get_even_numbers_iter(nums):
    """ if we were dealing with significantly large datasets
    it is recommended that you return a generator instead
    """
    for n in nums:
        if n % 2 == 0:
            yield n


if __name__ == '__main__':
    numbers = [x for x in range(1, 101)]
    # result = get_even_numbers(numbers)
    result = list(get_even_numbers_iter(numbers))
    print(result[:6])
