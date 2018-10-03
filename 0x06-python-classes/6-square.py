#!/usr/bin/python3
class Square:
    """this is a class Square that defines a square
    Attributes:
       __size: Private instance attribute - size of square
       __position: Private instance attribute - position of square
    Args:
       size: size of square.
       position: position of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """This is a function that use __init__ method to
        initialize the passing variables
        Attributes:
             __size: Private instance attribute - size of square
             __position: Private instance attribute - position of square
        Args:
             size: size of square.
             position: position of square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        meg = "position must be a tuple of 2 positive integers"
        if isinstance(position, tuple) and len(position) == 2:
            if position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                raise TypeError(meg)
        else:
            raise TypeError(meg)

    @property
    def size(self):
        """Getter: get size of square
        Return:
           return the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: set the argument value to size
        Attributes:
             __size: Private instance attribute - size of square
        Args:
             size: size of square
        Raises:
             TypeError: size must be an integer
             ValueError: size must be >= 0
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        return self.__size

    @property
    def position(self):
        """Getter: get position of square
        Return:
           return the position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter: set the argument value to size
        Attributes:
             __size: Private instance attribute - size of square
             __position: Private instance attribute - position of square
        Args:
             size: size of square
             position: position of square
        Raises:
             TypeError: position must be a tuple of 2 positive integers
        """
        meg = "position must be a tuple of 2 positive integers"
        if isinstance(value, tuple) and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError(meg)
        else:
            raise TypeError(meg)

    def area(self):
        """ This is a function calculate the area of a square
        Attributes:
             __size: Private instance attribute - size of square
        Returns:
             the result
        """
        return self.__size ** 2

    def my_print(self):
        """This function print a square"""
        if self.__size == 0:
            print()
        for x in range(0, self.__position[1]):
            print()
        for y in range(0, self.__size):
            print("{}".format(" " * self.__position[0]), end="")
            print("{}".format("#" * self.__size))
