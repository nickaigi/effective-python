# how tp zip two lists
from itertools import zip_longest


if __name__ == '__main__':
    names = ['nickson', 'newton', 'benson']

    num_of_letters = [7, 5, 6]

    for name, count in zip(names, num_of_letters):
        print('{} - {}'.format(name, count))

    # if the lists are of different lengths,
    # python will only zip upto the equal length portion
    print('lets add a name, but ommit to add it num_of_letters counterpart')
    names.append('macintosh')
    for name, count in zip(names, num_of_letters):
        print('{} - {}'.format(name, count))

    print('Python has zip_longest to tackle such scenarios')
    # zip_longest(list_one, list_two, fillvalue='xx')
    # fillvalue will be printed when there exists a length difference between
    # the two lists.
    for name, count in zip_longest(names, num_of_letters, fillvalue='-'):
        print('{} - {}'.format(name, count))
