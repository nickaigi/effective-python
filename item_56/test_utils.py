"""Demonstrates how to write unittests

    - Tests are organized into TestCase classes
    - Each test is a method beginning with the word 'test'

Consider using
    - Nose https://nose.readthedocs.io/en/latest/
    - pytest https://docs.pytest.org/en/latest/
"""
from unittest import TestCase, main
from utils import to_str


class UtilsTestCase(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))

    def test_to_str_bad(self):
        self.assertRaises(TypeError, to_str, object())


if __name__ == '__main__':
    main()
