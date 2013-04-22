# Python unit testing

from calculator import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(7,4), 3)

    def test_multiply(self):
        self.assertEqual(multiply(6,7), 42)

    def test_divide(self):
        self.assertEqual(divide(3,2), 1.5)

if __name__ == '__main__':
    unittest.main()
