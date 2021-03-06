#!/usr/bin/python3
class Rectangle:
    """This is a class Rectangle that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This is a function that use __init__ method to
        initialize the passing variables
        Args:
             width: width of rectangle
             height: height if rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter: get width of rectangle
        Return:
              return the width of rectangle
        """
        return self.__width

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of rectangle
        Return:
             return the area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """calculate the perimeter of rectangle
        Return:
             return the perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """print a rectangle
        Return:
             return a string
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        return (row + "\n") * (self.__height - 1) + row

    def __repr__(self):
        """print the height and width of a rectangle
        Return:
             return a string with height and width
        """
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """print bye message and decrease the number of instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """find the biggest rectangle based on the area
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle
        Return:
            return the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width = height = size
        """
        cls.number_of_instances += 1
        return Rectangle(size, size)
