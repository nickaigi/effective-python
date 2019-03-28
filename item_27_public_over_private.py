"""
Private fields are specified by prefixing an attribute's name with a double
underscore.

They can be accessed directly by methods of the containing class


Private attrib behaviour is implemented witha a simple transformation of the
attribute name.

    __private_field transforms to  _ClassName__private_field.

Why doesn't the syntax for private attributes actually enforce strict visibility?

-> We are all consenting adults here

ROFLOL

"""


class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field


class MyParentObject(object):
    """A subclass can not access its parents class's private field
    """
    def __init__(self):
        self.__private_field = 71


class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field


def main():
    foo = MyObject()
    assert foo.public_field == 5
    assert foo.get_private_field() == 10

    bar = MyOtherObject()
    assert bar.get_private_field_of_instance(bar) == 71

    baz = MyChildObject()
    # trying to access a private field that is set by the parent
    # will result in an attribute error
    try:
        baz.get_private_field()
    except AttributeError as e:
        print('A child can not access its parents private fields')

    # we can access the private field of the parent using the name transform
    assert baz._MyParentObject__private_field == 71
    print(baz.__dict__)  # {'_MyParentObject__private_field': 71


if __name__ == '__main__':
    main()
