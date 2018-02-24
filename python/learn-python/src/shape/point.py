import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    def __str__(self):
        return self.__repr__()

    def length(self, p):
        return math.sqrt(pow(self.x - p.x, 2) + pow(self.y - p.y, 2))


class Rectangle:
    def __init__(self, pts):
        self.points = pts
        min_x = max_x = pts[0].x
        min_y = max_y = pts[0].y
        for p in pts:
            if p.x < min_x:
                min_x = p.x
            if p.x > max_x:
                max_x = p.x
            if p.y < min_y:
                min_y = p.y
            if p.y > max_y:
                max_y = p.y
        self.ul = Point(max_x, min_y)
        self.lr = Point(min_x, max_y)

    def __repr__(self):
        return repr(self.ul) + "," + repr(self.lr)

    def __str__(self):
        return self.__repr__()

    def area(self):
        return (self.ul.x - self.lr.x) * (self.lr.y - self.ul.y)

    def point_inside(self, p):
        return (self.lr.x < p.x < self.ul.x) and (self.lr.y > p.y > self.ul.y)

    def overlaps(self, other):
        for p in other.points:
            if self.point_inside(p):
                return True
        return False
