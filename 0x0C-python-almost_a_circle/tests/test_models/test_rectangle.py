#!/usr/bin/python3
"""Unittest for class Rectangle
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_id_no_input(self):
        """test id with no input"""
        Base._Base__nb_objects = 0
        b1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.id, Rectangle._Base__nb_objects)
        b2 = Rectangle(1, 1, 1, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.id, Rectangle._Base__nb_objects)

    def test_id_datatype(self):
        """test id with different data type"""
        b3 = Rectangle(1, 1, 1, 1, 12)
        self.assertEqual(b3.id, 12)
        b4 = Rectangle(1, 1, 1, 1, "string")
        self.assertEqual(b4.id, "string")
        b5 = Rectangle(1, 1, 1, 1, {id:1})
        self.assertEqual(b5.id, {id:1})
        b7 = Rectangle(1, 1, 1, 1, [1])
        self.assertEqual(b7.id, [1])
        b8 = Rectangle(1, 1, 1, 1, 2.4)
        self.assertEqual(b8.id, 2.4)
        b9 = Rectangle(1, 1, 1, 1, (1,2))
        self.assertEqual(b9.id, (1,2))
        b10 = Rectangle(1, 1, 1, 1, {1,2})
        self.assertEqual(b10.id, {1,2})
        b11 = Rectangle(1, 1, 1, 1, True)
        self.assertEqual(b11.id, True)
        b12 = Rectangle(1, 1, 1, 1, False)
        self.assertEqual(b12.id, False)

    def test_id_special_case(self):
        """test id with special cases"""
        bN = Rectangle(1, 1, 1, 1, None)
        self.assertEqual(bN.id, 3)
        self.assertEqual(bN.id, Rectangle._Base__nb_objects)        
        b6 = Rectangle(1, 1, 1, 1, float('nan'))
        self.assertNotEqual(b6.id, b6.id)
        b6 = Rectangle(1, 1, 1, 1, float('inf'))
        self.assertEqual(b6.id, float('inf'))
    
    def test_width_height_int_success(self):
        """test width and height with integer that is greater than 0"""
        b1 = Rectangle(2, 1)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 1)
        b2 = Rectangle(3, 4, 1, 1)
        self.assertEqual(b2.width, 3)
        self.assertEqual(b2.height, 4)
        b3 = Rectangle(23, 40, 1, 1, 12)
        self.assertEqual(b3.width, 23)
        self.assertEqual(b3.height, 40)

    def test_width_height_int_fail(self):
        """test width and height with integer that is equal or less
        than 0
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_width_height_special_case(self):
        """test width and height with special cases"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'), 1)

    def test_width_isInt(self):
        """test width with non int data type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1:2}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", "b")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)

    def test_height_isInt(self):
        """test height with non int data type"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "a")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1,2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1,2])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1:2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, False)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", "b")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 2.4)

    def test_x_y_int_success(self):
        """test x and y with integer that is greater or equal 0"""
        b1 = Rectangle(2, 1, 2, 2)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 2)
        b2 = Rectangle(3, 4, 3, 4)
        self.assertEqual(b2.x, 3)
        self.assertEqual(b2.y, 4)
        b3 = Rectangle(23, 40, 23, 40, 12)
        self.assertEqual(b3.x, 23)
        self.assertEqual(b3.y, 40)
        b4 = Rectangle(23, 40, 0, 0, 0)
        self.assertEqual(b4.x, 0)
        self.assertEqual(b4.y, 0)

    def test_x_y_int_fail(self):
        """test x and y with integer that is less
        than 0
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, -1)

    def test_x_y_special_case(self):
        """test x and y with special cases"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('inf'), 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, float('inf'), 1)
        
    def test_x_isInt(self):
        """test x with non int data type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "a", 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {1}, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, [1], 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {1:2}, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, (1, 2), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, True, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, False, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "a", "b")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, 1.5, 2)

    def test_y_isInt(self):
        """test y with non int data type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, "a")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {1,2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, [1,2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {1:2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (1, 2))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "a", "b")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, 2.4)

    def test_area(self):
        """test area of rectangle"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(2, 2, 0, 0).area(), 4)

    def test_display(self):
        """test display method"""
        
if __name__ == '__main__':
    unittest.main()
