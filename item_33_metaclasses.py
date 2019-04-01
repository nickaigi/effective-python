""" metaclasses can be used to verify that a class was defined correctly.

use Meta.__new__ to validate instances of a class before its defined
"""

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        pprint((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    """
    Creating an instance of this class will demostrate that the Meta class has access to all its members
    >>> my_class = MyClass()
    (<class '__main__.Meta'>,
    'MyClass',
    (<class 'object'>,),
    {'__module__': '__main__',
     '__qualname__': 'MyClass',
     'foo': <function MyClass.foo at 0x7fcac70d5840>,
     'stuff': 123})
    """
    stuff = 123

    def foo(self):
        pass


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # we don't want to validate the abstract polygon class
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides -2) * 180


class Triangle(Polygon):
    sides = 3


def main():
    print('before class')
    class Line(Polygon):
        print('before sides')
        sides = 1
        print('after sides')

    print('after class')



if __name__ == '__main__':
    main()
