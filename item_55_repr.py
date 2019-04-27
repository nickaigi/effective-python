"""repr: how to use it

- calling 'print' produces printable human readable string version of the
  value, hides info

- calling 'repr' produces printable string version of the value, can be passed
  to 'eval'

- %s in format strings will produce human readable-strings like str

- %r will produce printable strings like repr

- add a __repr__ to customize the printable representation of a class

- if you can not customize the class, you can use the object's __dict__ attrib
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
    # use eval with caution
    b = eval(repr(a))
    assert a == b
    print(repr(5))
    print(repr('5'))

    # using repr is equivalent to using %r
    print('%r' % 5)
    print('%r' % '5')


class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def example_three():
    """
    >>> 
    <__main__.OpaqueClass object at 0x7f8a40223940>
    """
    obj = OpaqueClass(1, 2)
    print(obj)


class BetterClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)


def example_four():
    """
    >>> 
    BetterClass(1, 2)
    """
    obj = BetterClass(1, 2)
    print(obj)


def example_five():
    """
    >>> 
    {'x': 1, 'y': 2}
    """
    obj = OpaqueClass(1, 2)
    print(obj.__dict__)


def main():
    example_five()


if __name__ == '__main__':
    main()
