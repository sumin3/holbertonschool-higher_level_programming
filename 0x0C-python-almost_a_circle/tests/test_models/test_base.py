#!/usr/bin/python3
"""Unittest for class base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    def test_id(self):
        """test id of base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.id, Base._Base__nb_objects)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.id, Base._Base__nb_objects)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base("string")
        self.assertEqual(b4.id, "string")
        b5 = Base({id:1})
        self.assertEqual(b5.id, {id:1})
        b6 = Base(float('nan'))
        self.assertNotEqual(b6.id, b6.id)
        b7 = Base([1])
        self.assertEqual(b7.id, [1])
        b8 = Base(2.4)
        self.assertEqual(b8.id, 2.4)
        b9 = Base((1,2))
        self.assertEqual(b9.id, (1,2))
        b10 = Base({1,2})
        self.assertEqual(b10.id, {1,2})
        b11 = Base(None)
        self.assertEqual(b11.id, 3)
        self.assertEqual(b11.id, Base._Base__nb_objects)

    def test_to_json_string(self):
        """test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        json_dict = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(type(json_dict), str)
if __name__ == '__main__':
    unittest.main()
    
