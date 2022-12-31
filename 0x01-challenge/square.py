#!/usr/bin/python3
"""Module for class square
"""


class square():
    """class square
    Args:
        width (int):
        height (int):
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialiwation
        Args:
            args (list):
            kwargs (dict):
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.height)

    def PermiterOfMySquare(self):
        """Perimeter of the square
        """
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """representation
        """
        return ("{}/{}".format(self.width, self.height))


if __name__ == "__main__":
    """entry
    """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
