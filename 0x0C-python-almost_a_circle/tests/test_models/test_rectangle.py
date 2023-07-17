#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest
from io import StringIO
import sys as system


"""
This file contains the test file for the rectangle class
"""


class RectangleTestClass(unittest.TestCase):
    """
    This is the class that performs the test
    """

    def test_input_for_rectangle(self):
        """
        This tests the input for rectangle class
        """
        newInst = Rectangle(10, 5, 4, 5)
        self.assertEqual(newInst.id, 10)

    def test_setter_for_rectangle(self):
        """
        This tests the setter function for the rectangle
        """
        newInst = Rectangle(10, 5, 4, 5)
        localval = newInst
        newval_h = 3
        newval_w = 2
        newval_x = 0
        newval_y = 0
        localval.width = newval_w
        localval.height = newval_h
        localval.x = newval_x
        localval.y = newval_y
        self.assertEqual(localval.height, newval_h)
        self.assertEqual(localval.width, newval_w)
        self.assertEqual(localval.x, newval_x)
        self.assertEqual(localval.y, newval_y)

    def test_newInstanc(self):
        """
        This tests for the new isntance chnaging the ID
        """
        localNewInst = Rectangle(10, 34, id=9)
        self.assertEqual(localNewInst.id, 9)

    def test_wrong_type(self):
        """
        This tests for the wrong value and wrong type
        """
        localinst = Rectangle(10, 5, 4, 5)
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

    def test_area_functionality(self):
        """
        Find area of the rectangle
        """
        newLocalInst = Rectangle(90, 2, 0, 0, 1003)
        area = newLocalInst.area()
        self.assertEqual(area, 180)
        self.assertEqual(newLocalInst.id, 1003)

    def test_display_of_rectangle(self):
        """
        Test the display of rectangle
        """
        localvar = Rectangle(2, 2)
        pipedOutput = StringIO()
        system.stdout = pipedOutput
        localvar.display()
        output = pipedOutput.getvalue()
        system.stdout = system.__stdout__
        testoutput = "##\n##\n"
        self.assertEqual(output, testoutput)

    def test_string_repersentation(self):
        """
        Tests the string representation of the instance
        """
        newInst = Rectangle(10, 5, 4, 5)
        local_instance = newInst
        output = "[Rectangle] (12) 4/5 - 10/5"
        self.assertEqual(str(local_instance), output)

    def test_update_info(self):
        """
        This tests the update info for the class
        """
        newinst = Rectangle(2, 4, 6, 7, 10)
        self.assertEqual(newinst.id, 10)
        newinst.update(1, 2, 3, 4, 5)
        self.assertTrue(newinst.height == 3, True)
        self.assertTrue(newinst.id == 1, True)
        self.assertTrue(newinst.area() == 6, True)
        newinst.update(height=10, x=3, id=5)
        self.assertTrue(newinst.height == 10, True)
        self.assertTrue(newinst.id == 5, True)

    def test_to_dict(self):
        """
        This tests the object regarding the expression of
        the dictionary representation of a Rectangle
        """
        newInst = Rectangle(10, 10, id=50)
        self.assertTrue(type(newInst.to_dictionary()) == dict)
        dict_local = {
            "id": newInst.id,
            "width": newInst.width,
            "height": newInst.height,
            "x": newInst.x,
            "y": newInst.y
            }
        self.assertDictEqual(dict_local, newInst.to_dictionary())
