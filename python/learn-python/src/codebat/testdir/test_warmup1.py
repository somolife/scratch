import unittest


class TestWarmup1(unittest.TestCase):
    def test_max_span(self):
        from codebat.warmup1 import sleep_in
        self.assertTrue(sleep_in(False, False))
        self.assertFalse(sleep_in(True, False))

    def test_front3(self):
        from codebat.warmup1 import front3
        self.assertEqual("helhelhel", front3("hello"))
