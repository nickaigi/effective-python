class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo(object):
    def __init__(self):
        self.value *=2


class PlusFive(object):
    def __init__(self):
        self.value +=5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *=5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value +=2


class ThisWay(TimesFive, PlusTwo):
    """ Demonstrates a Diamond inheritance.
    This is when a subclass inherits from two separate classes,
    that have the same superclass somewhere in the hierarchy.
    """
    def __init__(self, value):
        TimesFive.__init__(self,value)
        PlusTwo.__init__(self, value)


class TimesFiveCorrect(MyBaseClass):
    """
    - Python 2.2 added the 'super' built in method and defined the MRO
    MRO Method Resolution Order

    - MRO standardizes which superclasses are initialized before others
    depth-first, left-to-right

    - Here we use the Python2 style call to super
    """
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *=5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value +=2

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    """
    - The order seems backwards... shouldn't TimesFiveCorrect.__init__ have run first?
    Inspecting the MRO for this class, we find the answer

    >>> from pprint import pprint
    >>> pprint(GoodWay.mro())
    [<class '__main__.GoodWay'>,
     <class '__main__.TimesFiveCorrect'>,
     <class '__main__.PlusTwoCorrect'>,
     <class '__main__.MyBaseClass'>,
     <class 'object'>]

    - Calling GoodWay(5)
        it calls TimesFiveCorrect.__init__ which calls PlusTwoCorrect.__init__
        which calls MyBaseClass.__init__

    - Once this reaches the top of the diamond, then all the inits do their
    work in the opposite order from how their __init__ functions were called
    bottom up.
    """
    def __init__(self, value):
        super(GoodWay, self).__init__(value)

class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value *2)


class Implicit(MyBaseClass):
    """Python3 style to call super"""
    def __init__(self, value):
        super().__init__(value * 2)


def main():
    # foo = OneWay(5)
    # print('First ordering is (5 *2) + 5 =', foo.value)
    # bar = AnotherWay(5)
    # print('Second ordering is still ', bar.value)
    # foo = ThisWay(5)
    # print('Should be (5 *  5) + 2 = 27 but is', foo.value)

    foo = GoodWay(5)
    print('Should be 5 * (5 + 2) = 35 and is', foo.value)
    assert Explicit(10).value == Implicit(10).value



if __name__ == '__main__':
    main()
