def log(message, *values):
    """ * operator instructs python to pass items from the sequence as
    positional arguments
    Remember:
        - using the * operator with a generator may cause your program
          to run out of memory and crash.

        - adding new positional parameters to functions that accept
          *args can introduce hard-to-find bugs
    """
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


if __name__ == '__main__':
    log('My numbers are', 1, 2)
    log('Hi there')

    favorites = [7, 33, 99]
    log('Favorites colors', *favorites)
