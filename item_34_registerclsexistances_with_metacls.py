"""
Another common use of metaclasses is to automatically register types in your
program
"""
import json

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
        return cls(*params['args'])


class BetterPoint2D(Desirializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterPoint2D(%d, %d)' % (self.x, self.y)


def main():
    point = Point2D(5, 3)
    print('Object:    ', point)
    print('Serialized:', point.serialize())


if __name__ == '__main__':
    main()
