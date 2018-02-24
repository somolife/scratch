import unittest


class TestList2(unittest.TestCase):
    def test_big_diff(self):
        from codebat.list2 import big_diff
        self.assertEqual(2, big_diff([2, 4]))
        self.assertEqual(4, big_diff([1,2, 4,5]))
