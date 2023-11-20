"""Intro To Object Oriented Programming."""
from __future__ import annotations

__author__ = "730529193"


class Point:
    """The home of the points and functions to mutate them."""
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Assigns initial values for the x and y attributes."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: float) -> None:
        """Mutates the points to scale by a specific factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Creates new points."""
        scale_x = self.x * factor
        scale_y = self.y * factor
        return Point(scale_x, scale_y)
    
    def __str__(self) -> str:
        """Returns a string representation of the Point."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Overloads the * operator for multiplication with a factor (int or float)."""
        return self.scale(float(factor))
    
    def __add__(self, factor: int | float) -> Point:
        """Overloads the + operator for addition with a factor (int or float)."""
        return Point(self.x + float(factor), self.y + float(factor))