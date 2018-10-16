#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area function, raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name: the name
            value: integer value
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.__name = name
        self.__value = value


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
