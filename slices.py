# Remember that everything in python is
# pass by reference


if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print('First four: ', a[:4])  # same as a[0:4]

    # -ve list index starts at position 1
    print('Last four: ', a[-4:])

    print('Middle two: ', a[3:-3])

    # when used in assignments, lists will grow/shrink to accomodate the new
    # values

    # remember a[x:y] is index x inclusive, y not inclusive

    print('Before : ', a)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # list items from index 2:7 will shrink to fit 3 items
    a[2:7] = [99, 22, 14]

    print('After : ', a)  # ['a', 'b', 99, 22, 14, 'h']
    # same applies to assignment of a slice with no start/end index

    # if you leave out the start/end index in a slice
    # you create a copy of the list
    b = a[:]
    assert b is not a

    # but if we were to assign b to a
    # a and b are references to the same object
    b = a
    a[:] = [100, 101, 102]

    assert a is b  # still the same object

    print('Second assignment : ', a)  # ['a', 'b', 99, 22, 14, 'h']
