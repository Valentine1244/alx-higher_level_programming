#!/usr/bin/python3
from models.square import Square
import unittest
import sys as system
from io import StringIO


"""
This file contains the unitest test for the Square class.
It tests all functions and cases for the File
"""


class TestSquareClass(unittest.TestCase):
    """
    The begining of unit test for the square
    """

    def test_init_method(self):
        """
        Tests the init menthod of the class since it inherits
        from a parent class
        """
        newlocalInst = Square(2, id=4)
        self.assertEqual(newlocalInst.height, 2)
        self.assertEqual(newlocalInst.width, 2)
        self.assertEqual(newlocalInst.id == 4, True)

    def test_display_representation(self):
        """
        Tests stdout representation of the object either it matchs
        """
        newlocalInst = Square(3, id=4)
        strngIO = StringIO()
        system.stdout = strngIO
        newlocalInst.display()
        output = strngIO.getvalue()
        system.stdout = system.__stdout__
        expectedOutput = "###\n###\n###\n"
        self.assertEqual(output, expectedOutput)

    def test_str_representataion(self):
        """
        Tests the string representation of the object
        """
        newlocalInst = Square(2)
        self.assertTrue(str(newlocalInst) == "[Square] (16) 0/0 - 2", True)

    def test_area(self):
        """
        Tests the area of the square if computed well
        """
        newlocalInst = Square(10)
        area = newlocalInst.area()
        self.assertEqual(area, 100)

    def test_wrong_type(self):
        """
        This tests for the wrong value and wrong type
        """
        localinst = Square(10, 5, 4)
        wrngTyp = "3"
        wrngVal = -1
        noneVal = None
        with self.assertRaises(TypeError):
            localinst.width = wrngTyp
            localinst.height = wrngTyp
            localinst.x = wrngTyp
            localinst.y = wrngTyp

        with self.assertRaises(ValueError):
            localinst.width, localinst.height = (wrngVal, wrngVal)
            localinst.x, localinst.y = (wrngVal, wrngVal)
            localinst.update(lol=10)

        with self.assertRaises(TypeError):
            localinst.height, localinst.width = (noneVal, noneVal)
            localinst.x, localinst.y = (noneVal, noneVal)

    def test_size_setter_for_Square(self):
        """
        This tests the setter function for the rectangle
        """
        localval = Square(10, 5, 4)
        newval_s = 3
        newval_x = 0
        newval_y = 0
        localval.size = newval_s
        localval.x = newval_x
        localval.y = newval_y
        self.assertEqual(localval.height, newval_s)
        self.assertEqual(localval.width, newval_s)
        self.assertEqual(localval.x, newval_x)
        self.assertEqual(localval.y, newval_y)

    def test_update_info(self):
        """
        This tests the update info for the class
        """
        newinst = Square(1, 6, 7, 10)
        self.assertEqual(newinst.id, 10)
        newinst.update(2, 4, 6, 11)
        self.assertTrue(newinst.height == 4, True)
        self.assertTrue(newinst.width == 4, True)
        self.assertTrue(newinst.id == 2, True)
        self.assertTrue(newinst.area() == 16, True)
        newinst.update(height=10, x=3, id=5)
        self.assertTrue(newinst.height == 10, True)
        self.assertTrue(newinst.id == 5, True)
        self.assertEqual(newinst.size == 4, True)

    def test_to_dict(self):
        """
        This tests the object regarding the expression of
        the dictionary representation of a Square
        """
        newInst = Square(10, id=50)
        self.assertTrue(type(newInst.to_dictionary()) == dict)
        dict_local = {
            "id": newInst.id,
            "size": newInst.size,
            "x": newInst.x,
            "y": newInst.y
            }
        self.assertDictEqual(dict_local, newInst.to_dictionary())
