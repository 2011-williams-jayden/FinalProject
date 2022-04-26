#Test Driver: Basic Calc Testing
#Date: 4/26/22
#Author: Jayden Williams

import unittest

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b
  
    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b

class TestCalculator(unittest.Calculator):
    def setUp(self):
        self.calc = Calculator()
  
    def test_add(self):
        '''Test case function for addition'''
        self.calc = Calculator()
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_sub(self):
        '''Test case function for subtraction'''
        self.calc = Calculator()
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    def test_mul(self):
        '''Test case function for multiplication'''
        self.calc = Calculator()
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)

    def test_div(self):
        '''Test case function for division'''
        self.calc = Calculator()
        result = self.calc.div(10, 2)
        expected = 5
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()