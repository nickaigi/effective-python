"""For APIs it's much more powerful to define your own hierarchy of exceptions"""


def determine_weight(volume, density):
    if density <= 0:
        raise ValueError('Density must be positive')
    pass


class Error(Exception):
    """Base-class for all exceptions  raised in this module."""


class InvalidDensityError(Erro):
    """There was a problem with a provided density value."""


def main():
    try:
        weight = determine_weight(1, -1)
    except Error as e:
        print('Unexpected error: %s', e)
