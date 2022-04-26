#Test Driver: Addition Testing
#Date: 4/26/22
#Author: Jayden Williams

import unittest
class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

class TestCalcAdd(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator()

    def test_add(self):
        '''Test case function for addition'''
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_add_integer_string(self):
        result = self.calculator.add(4, "9")
        self.assertEqual(result, "ERROR")

    def test_add_negative_integers(self):
        result = self.calculator.add(-8, -6)
        self.assertEqual(result, -14)
        self.assertNotEqual(result, 14)

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

if __name__ == '__main__':
    unittest.run()