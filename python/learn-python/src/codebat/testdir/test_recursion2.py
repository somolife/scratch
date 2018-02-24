import unittest


class TestRecursion2(unittest.TestCase):
    def test_group_sum(self):
        from codebat.recursion2 import group_sum
        self.assertTrue(group_sum(0, [1, 2, 3], 3))
        self.assertTrue(group_sum(0, [1, 2, 3, 4, 5], 7))

    def test_split_array(self):
        from codebat.recursion2 import split_array
        self.assertTrue(split_array([1, 2, 3]))
        self.assertTrue(split_array([5, 4, 1, 2, 3, 1, 4]))
