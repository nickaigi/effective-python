from decimal import Decimal
from decimal import ROUND_UP


def example_one():
    """
    >>> 
    5.364999999999999
    Rounded to:  5.36
    """
    rate = 1.45
    seconds = 3*60 + 42
    cost = rate * seconds / 60
    print(cost)
    # Round cost down to the nearest whole cent
    print('Rounded to: ', round(cost, 2))


def example_two():
    """
    >>> 
    0.004166666666666667
    Rounded to:  0.0
    """
    rate = 0.05
    seconds = 5
    cost = rate * seconds / 60
    print(cost)
    # The result float is so low that it rounds down to zero
    print('Rounded to: ', round(cost, 2))


def example_three():
    """
    >>> 
    5.365
    5.37
    """
    rate = Decimal('1.45')
    seconds = Decimal('222')  # 3*60 + 42
    cost = rate * seconds / Decimal('60')
    print(cost)
    rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
    print(rounded)


def example_four():
    """
    >>> 
    0.004166666666666666666666666667
    0.01
    """
    rate = Decimal('0.05')
    seconds = Decimal('5')
    cost = rate * seconds / Decimal('60')
    print(cost)
    rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
    print(rounded)


def example_five():
    """
    For representing rational numbers with no limit to precision, consider
    using the 'Fraction' class from the 'fractions' built-in module
    """
    # TODO
    pass


def main():
    example_four()


if __name__ == '__main__':
    main()
