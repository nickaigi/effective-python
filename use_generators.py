# I have not included how to use list comprehensions.
# use generators when dealing with large data that needs to be held in memory.
# generators can also be composed together
#

if __name__ == '__main__':
    a = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    it_squares = (x ** 2 for x in a)

    print(next(it_squares))  # will print 4
    # subsequent calls to next(it_squares) will traverse and eventually exhaust
    # the generator

    roots = ((x, x ** 0.5) for x in it_squares)
    # the single call to next for the outer generator,
    # will also advance the inne generator.
    print(next(roots))  # will print 2
