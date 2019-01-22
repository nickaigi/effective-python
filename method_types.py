# discussed in item 2: Follow PEP8 style guide
# demonstrates the difference between
# instance methods, class methods, and static methods


class Person(object):

    counter = 0  # class attribute

    def __init__(self, name):
        self.name = name
        type(self).counter += 1
        # type(self) will evaluate to Person
        # might as well write Person.counter
        # but type(self) is best especially when we inherit this class

    def speak(self):
        """ Instance method
        - receives self
        - thus can modify instance attributes
        """
        print('my name is {}'.format(self.name))

    @classmethod
    def number_of_people(cls):
        """ Class method
        - receives cls
        - uses @classmethod decorator
        - thus can modify class attributes attributes
        """
        print('we have created {} people'.format(cls.counter))

    @staticmethod
    def add(a, b):
        """ static method
        - uses @staticmethod decorator
        - has no access to self or cls
        - thus can not modify instance or class variables
        """
        print(' {} + {} = {}'.format(a, b, a + b))


if __name__ == '__main__':
    p1 = Person('Nick')
    p2 = Person('Guido')
    p3 = Person('Knuth')

    p1.speak()
    p2.speak()
    p3.speak()

    Person.number_of_people()
    Person.add(2, 3)
