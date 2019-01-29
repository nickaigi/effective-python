# demonstrate how to manipulate lists using the
#
# somelime[start:end:stride]
# avoid using start, end, stride in the same list
# it is confusing and hard to read
#
# stride represents every nth element, current index inclusive

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('the list: ', a[::])
    print('odds: ', a[::2])  # start at 0, end at end of list, implicit
    print('even: ', a[1::2])

    # the statement below is ugly, do not use.
    # we might as well have created
    # odds = a[::2]
    # then sliced the odds list
    # odds[2:4]
    print('odds start at index 2 upto index 8: ', a[2:8:2])

    # you can also use -ve indices to traverse the list in reverse
    # traversing the list using -ve indices starts at index -1

    # implicit start, end values. traverse from reverse with a stride of -1
    print('reversed: ', a[::-1])

    print('even from reverse: ', a[::-2])
