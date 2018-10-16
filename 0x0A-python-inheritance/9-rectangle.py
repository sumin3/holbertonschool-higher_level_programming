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


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """initialize the passing variables
        Args:
            width: the width
            height: the height
        Attributes:
            __width: width of rectangle
            __height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area
        Return:
            return the area
        """
        return self.__height * self.__width

    def __str__(self):
        """print rectangle description: [Rectangle] <width>/<height>
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
