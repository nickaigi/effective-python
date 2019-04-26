"""repr
"""


def example_one():
    """print outputs a human-readable string version of whatever you supply 
    to it
    - problem is that the human-readable string for a value doens'nt make it
      clear what the actual type of the value is.
    """
    print('foo bar')
    print('%s' % 'foo bar')

    print(5)
    print('5')


def example_two():
    a = '\x07'
    print(repr(a))


def main():
    example_two()


if __name__ == '__main__':
    main()
