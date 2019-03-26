import math


class Pizza(object):
    """ Demonstrates how to effectively use classmethod
    and the power of staticmethod
    """
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        # TODO what does __repr__ do
        # TODO what are f strings
        return (
            f'Pizza({self.radius!r}, '
            f'{self.ingredients!r})'
        )

    @classmethod
    def margherita(cls):
        return cls(5, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(8, ['mozzarella', 'tomatoes', 'ham'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


def main():
    margherita = Pizza.margherita()
    prosciutto = Pizza.prosciutto()

    print(margherita.area())
    print(Pizza.circle_area(4))


if __name__ == '__main__':
    main()
