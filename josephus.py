import sys


def winning_seat(total):
    if total <= 2:
        winner = 1
        return winner
    else:
        for x in range(1, total):
            if 2 ** (x + 1) > total:
                diff = total - (2 ** x)
                winner = (2 * diff) + 1
                return winner


if __name__ == '__main__':
    total = int(sys.argv[1])
    print(winning_seat(total))
