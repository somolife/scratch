import unittest


class TestString1(unittest.TestCase):
    def test_make_tags(self):
        from codebat.string1 import make_tags
        self.assertEqual("<i>Hey</i>", make_tags("i", "Hey"))
