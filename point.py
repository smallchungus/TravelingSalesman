from __future__ import annotations
import math

# (2D point data type to model points in the plane.)
class Point:
    # create the point (x, y)
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Returns a string representation of the point.
    # Should be in coordinate pair output with no spaces.
    # i.e. (x,y)
    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    # return Euclidean distance between the two points
    def distance_to(self, that: Point) -> float:
        dx = that.x - self.x
        dy = that.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance