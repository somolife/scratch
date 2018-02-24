import unittest


class TestArray3(unittest.TestCase):
    def test_max_span(self):
        from codebat.array3 import max_span
        self.assertEqual(1, max_span([1, 2, 3, 4]))
        self.assertEqual(4, max_span([1, 2, 3, 4, 2]))
