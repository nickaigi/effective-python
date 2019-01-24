# discussed in item 2: Follow PEP8 style guide
# demonstrates the difference between
# instance methods, class methods, and static methods

from enum import Enum


class Person(object):
    class Category(Enum):
        # Enum is not a class
        # https://docs.python.org/3/library/enum.html#how-are-enums-different
        student = 1
        teacher = 2

    counter = 0  # class attribute

    def __init__(self, name, age, category):
        self.name = name
        self.age = age
        self.category = category
        type(self).counter += 1
        # type(self) will evaluate to Person
        # might as well write Person.counter
        # but type(self) is best especially when we inherit this class

    def speak(self):
        """ Instance method
        - receives self
        - thus can modify instance attributes
        """
        print('{} - {} - {}'.format(self.name, self.age, self.category))

    @classmethod
    def number_of_people(cls):
        """ Class method
        - receives cls
        - uses @classmethod decorator
        - thus can modify class attributes attributes
        """
        print('we have created {} people'.format(cls.counter))

    @classmethod
    def teacher(cls, name, age):
        return cls(name, age, cls.Category.teacher)

    @classmethod
    def student(cls, name, age):
        return cls(name, age, cls.Category.student)

    @staticmethod
    def add(a, b):
        """ static method
        - uses @staticmethod decorator
        - has no access to self or cls
        - thus can not modify instance or class variables
        """
        print(' {} + {} = {}'.format(a, b, a + b))


if __name__ == '__main__':
    nick = Person.student('Nick', 30)
    nick.speak()

    don = Person.teacher('Don', 81)
    don.speak()

    Person.number_of_people()
    import pdb; pdb.set_trace()
