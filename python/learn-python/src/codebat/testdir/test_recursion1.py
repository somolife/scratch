import unittest


class TestRecursion1(unittest.TestCase):
    def test_triangle(self):
        from codebat.recursion1 import triangle
        self.assertEqual(6, triangle(3))
        self.assertEqual(10, triangle(4))
