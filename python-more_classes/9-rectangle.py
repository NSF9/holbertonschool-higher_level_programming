#!/usr/bin/python3
"""
Module: rectangle
Defines a Rectangle class with width, height,
area calculation, perimeter, and string representation.
"""


class Rectangle:
    """
    Represents a rectangle defined by width and height.
    """

    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width = 0, height = 0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): New height value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the rectangle area.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the rectangle perimeter.

        If width or height is 0, the perimeter is 0.

        Returns:
            int: The perimeter value.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.

        If width or height is 0, returns an empty string.

        Returns:
            str: The rectangle as a string of '#' characters.
        """
        if self.__width <= 0 or self.__height <= 0:
            return ""
        lines = []
        for i in range(self.__height):
            lines.append(f"{(self.print_symbol)}" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns the default object representation.

        This method uses the base 'object.__repr__()' implementation to display
        the technical memory address format, such as:
        <module_name.ClassName object at 0x...>

        Useful for debugging or when no custom representation is needed.

        Returns:
        str: The default representation of the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
       print("Bye rectangle...")
       Rectangle.number_of_instances -= 1
    
    
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1,Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2,Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        Area1 = rect_1.__width * rect_1.__height
        Area2 = rect_2.__width * rect_2.__height

        if Area1 > Area2:
            return rect_1
        elif Area1 < Area2:
            return rect_2
        else:
            rect_1
    @classmethod
    def square(cls, size=0):
        """this is an init for the Rectangle class """
        return cls(size,size)
    
