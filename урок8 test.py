import unittest

from урок8 import *

class My_test(unittest.TestCase):
    def test_args(self ):
        self.assertEqual(adder(2,2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=5,b=10), 17)

if __name__ == '__main__':
    unittest.main()