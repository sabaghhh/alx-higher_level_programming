#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class representation."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init base class and set properties"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_int(name, value):
        """validates integer value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

    @staticmethod
    def validate_greater_than_zero(name, value):
        """validates greater than zero value"""
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def validate_positive(name, value):
        """validates positive value"""
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, n_x):
        """setter for x"""
        self.validate_int("x", n_x)
        self.validate_positive("x", n_x)
        self.__x = n_x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, n_y):
        """setter for y"""
        self.validate_int("y", n_y)
        self.validate_positive("y", n_y)
        self.__y = n_y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, n_width):
        """setter for width"""
        self.validate_int("width", n_width)
        self.validate_greater_than_zero("width", n_width)
        self.__width = n_width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, n_height):
        """setter for height"""
        self.validate_int("height", n_height)
        self.validate_greater_than_zero("height", n_height)
        self.__height = n_height

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns the string representation of the rectangle instance"""
        id = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y

        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """updates the rectangle instance arguments"""
        if args:
            arg_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
