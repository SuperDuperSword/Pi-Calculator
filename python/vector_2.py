from __future__ import annotations
import math


class Vector2:
    x: float = 0
    y: float = 0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector2(self.x * other, self.y * other)

        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (1 / other)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        return self + (other * -1)

    @staticmethod
    def average(a: Vector2, b: Vector2):
        return Vector2((a.x + b.x) / 2, (a.y + b.y) / 2)

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self) -> Vector2:
        return self / self.length()

    def distance(self, other: Vector2):
        return (self - other).length()
