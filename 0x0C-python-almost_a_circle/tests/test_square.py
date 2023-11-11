#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Define unit test for Square model"""

    def setUp(self):
        # Reset the Base class's _Base__nb_objects counter before each test
        Base._Base__nb_objects = 0

    def test_initialization_success(self):
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, 1)  # First instance, so id should be 1
        self.assertEqual(s2.id, 2)  # Second instance, so id should be 2

    def test_initialization_without_arguments(self):
        with self.assertRaises(TypeError):
            Square()

if __name__ == '__main__':
    unittest.main()

