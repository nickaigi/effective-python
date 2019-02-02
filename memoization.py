# memoization is caching the result of an expensive function
# and using the cached result whenever the expensive function is called with
# the same arguments
import time
exp_result = {}


def expensive_func(num):
    if num in exp_result:
        return exp_result[num]

    time.sleep(10)
    result = num * num
    exp_result[num] = result
    return result


if __name__ == '__main__':
    result = expensive_func(10)
    print(result)
    result = expensive_func(4)
    print(result)

    # calling expensive func again with same argument, will return the cached
    # result instead of performing the expensive operation again
    result = expensive_func(10)
    print(result)
    result = expensive_func(4)
    print(result)
