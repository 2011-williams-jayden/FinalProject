#Test Driver: Addition Testing
#Date: 4/26/22
#Author: Jayden Williams

import unittest

class Calculator:
    def __init__(self):
        pass

    def sub(self, a, b):
        return a - b


class TestCalcSub(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator()

    def test_sub(self):
        '''Test case function for addition'''
        self.assertEqual(self.calc.sub(15, 5), 10)
        self.assertEqual(self.calc.sub(7, 2), 5)

    def test_sub_integer_string(self):
        result = self.calculator.sub(12, "9")
        self.assertEqual(result, "ERROR")

    def test_sub_negative_integers(self):
        result = self.calculator.sub(2, 3)
        self.assertEqual(result, -1)
        
    def test_sub_zero(self):
        result = self.calculator.sub(4, 4)
        self.assertEqual(result, 0)

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

if __name__ == '__main__':
    unittest.run()