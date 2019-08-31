# Python
import os
import sys
import unittest


class TestAutoDotEnv(unittest.TestCase):

    def test_imported(self):
        print(sys.path)
        self.assertTrue('autodotenv' in sys.modules)

    def test_foo(self):
        self.assertFalse(os.environ.get('AUTODOTENV_TEST'))
        print(os.getcwd())


suite = unittest.TestLoader().loadTestsFromTestCase(TestAutoDotEnv)
