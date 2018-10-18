#!/usr/bin/python3
from models.base import Base
"""import class Base"""

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method: initialize the passing variables
        Args:
             width: width of rectangle
             height: height of rectangle
             x: x position of rectangle
             y: y position of rectangle
             id: id of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        "Getter: get width of the rectangle"""
        return self__width

    @width.setter
    def width(self, value):
        """Setter: set the argument value to width
        Attributes:
              ___width: width of rectangle
        Args:
              value: width of rectangle
        Raises:
              TypeError: width must be an integer
              ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter: get height of rectangle
        Return:
             return the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: set the argumet value to height
        Attributes:
               __height: the height of rectangle
        Args:
               value: the height of rectangle
        Raises:
               TypeError: height must be an integer
               ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter: get x position of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter: set argument value to x
        Attributes:
               __x: the x position of rectangle
        Args:
               value: the x position of rectangle
        Raises:
               TypeError: x must be an integer
               ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter: get y position of rectangle"""
        return self.__y

    @x.setter
    def y(self, value):
        """Setter: set argument value to y
        Attributes:
               __y: the y position of rectangle
        Args:
               value: the y position of rectangle
        Raises:
               TypeError: y must be an integer
               ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area method: calculate the area of rectangle
        Return:
           return the area
        """
        return self.__width * self.__height
    
    def display(self):
        """display method: prints in stdout the Rectangle instance
        with the character # by taking care of x and y position
        """
        print(self.__y * '\n', end="")
        row = self.__x * ' ' + self.__width * '#'
        print("\n".join([row for h in range(self.__height)]))

    def __str__(self):
        """__str__ method: return a string
        Return:
            return [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args):
        """update method: assigns an argument to each attribute
        Args:
           args: argument
        """
        
