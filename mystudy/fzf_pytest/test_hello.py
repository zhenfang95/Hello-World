#!/usr/bin/env python
import unittest

class Test1(unittest.TestCase):
    def test_helo(self):
        print('hello world')

if __name__ == '__main__':
    unittest.main()