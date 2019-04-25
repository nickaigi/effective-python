def palindrome(word):
    """Return True if the given world is a palindrome"""
    return word == word[::-1]


def main():
    print(repr(palindrome.__doc__))


if __name__ == '__main__':
    main()
