class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer(object):
    """
    >>> foo = Customer()
    >>> print('Before:', repr(foo.first_name), foo.__dict__)
    Before: '' {}
    >>> foo.first_name = 'Euclid'
    >>> print('After: ', repr(foo.first_name), foo.__dict__)
    After:  'Euclid' {'_first_name': 'Euclid'}
    """
    # class attributes
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')


class GoodField(object):
    def __init__(self):
        # these will be assigned by the metaclass.
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, GoodField):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DatabaseRow(object, metaclass=Meta):
    pass


class BetterCustomer(DatabaseRow):
    """ By using the metaclass, the new DatabaseRow base class, and the new
    GoodField descriptor, the class defination for a database row no longer has
    the redundancy from before
    """
    first_name = GoodField()
    last_name = GoodField()
    prefix = GoodField()
    suffix = GoodField()


def main():
    foo = BetterCustomer()
    print('Before:', repr(foo.first_name), foo.__dict__)
    foo.first_name = 'Euler'
    print('After: ', repr(foo.first_name), foo.__dict__)


if __name__ == '__main__':
    main()
