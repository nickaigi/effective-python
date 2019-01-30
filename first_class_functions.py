# A first classs citizen in a programming language is an entity which supports
# all the operations generally available to other entities.
#
# the operations include:
#     1. it can be assigned to a variable
#     2. Can be passed as an argument
#     3. Can be returned from a function
#     4. Can be returned tested for equality


def square(x):
    return x * x


def cube(x):
    return x * x * x


def my_map(func, args):
    result = []
    for i in args:
        result.append(func(i))
    return result


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(my_map(square, a))
    print(my_map(cube, a))
