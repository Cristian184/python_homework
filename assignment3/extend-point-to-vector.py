import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    v1 = Vector(1, 1)
    v2 = Vector(2, 2)

    print(p1, "==", p2, "?", p1 == p2)
    print("Distance between points:", p1.distance(p2))
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector sum:", v1 + v2)