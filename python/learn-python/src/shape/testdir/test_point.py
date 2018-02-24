import unittest

from shape.point import Point, Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle([Point(0, 0), Point(0, 2), Point(3, 0), Point(3, 2)])
        self.assertEqual(6, r.area())

    def test_point_inside(self):
        r = Rectangle([Point(0, 0), Point(0, 2), Point(3, 0), Point(3, 2)])
        self.assertTrue(r.point_inside(Point(1, 1)))
        self.assertFalse(r.point_inside(Point(1, 2)))

    def test_overlaps(self):
        r1 = Rectangle([Point(0, 0), Point(0, 2), Point(3, 0), Point(3, 2)])
        r2 = Rectangle([Point(1, 1), Point(1, 3), Point(2, 1), Point(2, 3)])
        self.assertTrue(r1.overlaps(r2))
        r3 = Rectangle([Point(4, 4), Point(4, 5), Point(6, 4), Point(6, 5)])
        self.assertFalse(r1.overlaps(r3))
