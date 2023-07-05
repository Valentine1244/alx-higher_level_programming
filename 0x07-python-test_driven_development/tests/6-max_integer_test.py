#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_isNone(self):
        self.assertIsNone(max_integer([]))

    def test_highestval(self):
        maxval = max_integer([1,2,3,4,5])
        self.assertEqual(maxval, 5)

    def test_isNotNone(self):
        self.assertIsNotNone(max_integer([1,2,3,4]))
    
    def test_isanInt(self):
        maxval = max_integer([1,2,3,4,5])
        self.assertTrue(type(maxval) == int)
