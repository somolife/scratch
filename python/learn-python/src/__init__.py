import unittest

loader = unittest.TestLoader()
unittest.TextTestRunner(verbosity=2).run(loader.discover('.', pattern='test*.py'))
