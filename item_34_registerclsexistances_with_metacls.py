"""
Another common use of metaclasses is to automatically register types in your
program
"""
import json

registry = {}


class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)


class Desirializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])


class BetterPoint2D(Desirializable):
    """ The problem with this approach is that it only works if you know the
    intended type of the serialized data ahead of time

    >>> point = BetterPoint2D(5, 3)
    >>> print('Before:    ', point)
    Before:     BetterPoint2D(5, 3)
    >>> data = point.serialize()
    >>> print('Serialized:', data)
    Serialized: {"args": [5, 3]}
    >>> after = BetterPoint2D.deserialize(data)
    >>> print('After:    ', after)
    After:     BetterPoint2D(5, 3)

    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterPoint2D(%d, %d)' % (self.x, self.y)


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })

    def __repr__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join(str(x) for x in self.args))


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class EvenBetterPoint2D(BetterSerializable):
    """ Works like this
    >>> point = EvenBetterPoint2D(5, 3)
    >>> print('Before:   ', point)
    >>> data = point.serialize()
    >>> print('Serialized:', data)
    >>> after = deserialize(data)
    >>> print('After:    ', after)
    Before:    EvenBetterPoint2D(5, 3)
    Serialized: {"class": "EvenBetterPoint2D", "args": [5, 3]}
    After:     EvenBetterPoint2D(5, 3
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


register_class(EvenBetterPoint2D)


class Point3D(BetterSerializable):
    """ Try this
    >>> point = Point3D(5, 9, -4)
    >>> data = point.serialize()
    >>> deserialize(data)
    KeyError: 'Point3D'

    KeyError because we forgot to register_class
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z


def main():
    pass


if __name__ == '__main__':
    main()
