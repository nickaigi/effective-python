"""For APIs it's much more powerful to define your own hierarchy of exceptions

1. root exceptions let callers understand when there's a problem with their
   usage of your API
"""


def determine_weight(volume, density):
    if density <= 0:
        raise ValueError('Density must be positive')
    pass


class Error(Exception):
    """Base-class for all exceptions  raised in this module."""


class InvalidDensityError(Erro):
    """There was a problem with a provided density value."""


def example_one():
    try:
        weight = determine_weight(1, -1)
    except Error as e:
        print('Unexpected error: %s', e)


def example_two():
    try:
        weight = determine_weight(1, -1)
    except InvalidDensityError:
        weight = 0
    except Error as e:
        print('Bug in the calling code: %s', e)


def example_three():
    try:
        weight = determine_weight(1, -1)
    except InvalidDensityError:
        weight = 0
    except Error as e:
        print('Bug in the calling code: %s', e)
    except Exception as e:
        print('Bug in the API code: %s', e)
        raise


class NegativeDensityError(InvalidDensityError):
    """When provided density value is negative"""


def new_determine_weight(volume, density):
    if density < 0:
        raise NegativeDensityError


def main():
    example_three()
