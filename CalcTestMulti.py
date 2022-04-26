#Test Driver: Multiplication Testing
#Date: 4/26/22
#Author: Jayden Williams

import unittest
import Calculator

class Calculator:
    def __init__(self):
        pass
  
    def mul(self, a, b):
        return a * b


class TestCalcMulit(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator(input(3))

    def test_mult(self):
        '''Test case function for division'''
        self.assertEqual(self.calc.mul(2, 7), 14)
        self.assertEqual(self.calc.mul(12, 2), 24)

    def test_mult_integer_string(self):
        result = self.calculator.mul(7, "x")
        self.assertEqual(result, "ERROR")

    def test_mult_negative_integers(self):
        result = self.calculator.mul(-3, 2)
        self.assertEqual(result, -6)
    
    def test_mult_double_negative_integers(self):
        result = self.calculator.mul(-3, -3)
        self.assertEqual(result, 9)
        self.assertNotEqual(result, -9)        

    def test_mult_integer_zero(self):
        result = self.calculator.mul(3, 0)
        self.assertEqual(result, 0)
        self.assertNotEqual(result, 3) 
        self.assertNotEqual(result, 1)

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

if __name__ == '__main__':
    unittest.main()