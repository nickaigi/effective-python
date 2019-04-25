"""Library for testing words for various linguistic patterns.

Testing how words relate to each other can be tricky sometimes!
This module provides easy ways to determine when words you've found have
special properties.

Available functions:
- palindrome: Determine if a word is a palindrome
  a palindrom is a word that has the same meaning when written in reverse
  e.g. nun

- check_anagram: determine if two words are anagrams.
  e.g. orchestra and carthorse

PEP 257 for best-practices for docstrings
"""



def palindrome(word):
    """Return True if the given world is a palindrome"""
    return word == word[::-1]


def find_anagrams(word, dictionary):
    """Find all anagrams for a word.

    This functionality only runs as fast as the test for membership in the
    'dictionary' container. It will be slow if the dictionary is a list and
    fast if it's a set.

    Args:
        word: String of the target word.
        dictionary: Container with all strings that are known to be actual
            words.

    Returns:
        List of arguments tht were found. Empty if none were found
    """
    # TODO
    pass


def example_x():
    """Once you've written docstrings for your modules, it's important to keep
    the documentaiton up to date.
    The 'doctest' built-in module makes it easy to exercis usage examples
    embedded in docstrings to ensure that your source code and its documentaiton doesn't diverge over time.
    """
    # TODO: learn about doctest and sphinx
    pass


def main():
    print(repr(palindrome.__doc__))


if __name__ == '__main__':
    main()
