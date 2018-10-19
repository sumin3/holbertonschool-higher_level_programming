
#!/usr/bin/python3
from models.rectangle import Rectangle
"""import class rectangle"""


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method: initialize the passing variables
        Args:
            size: size of square
            x: x position of square
            y: y position of square
            id: id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method: return a string
        Return:
            return [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
        
    @property
    def size(self):
        """Getter: get size of square
        Return:
            return size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter: set argument value to size
        Args:
           value: size of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        
