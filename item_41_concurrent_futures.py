from time import time


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def example_one():
    numbers = [
        (1963309, 2265973), (2030677, 3814172), (1551645, 2229620),
        (2039045, 2020802)
    ]


def main():
    example_one()


if __name__ == '__main__':
    main()
