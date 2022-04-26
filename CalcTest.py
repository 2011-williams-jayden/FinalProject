#Test Driver: Basic Calc Testing
#Date: 4/26/22
#Author: Jayden Williams

import unittest
import Calculator

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

class TestCalcAdd(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator(input(1))

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

class TestCalcSub(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator(input(4))

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

class TestCalcDiv(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator(input(4))

    def test_div(self):
        '''Test case function for division'''
        self.assertEqual(self.calc.div(10, 5), 2)
        self.assertEqual(self.calc.div(12, 2), 6)

    def test_div_negative_integers(self):
        result = self.calculator.div(-8, 2)
        self.assertEqual(result, -4)

    def test_div_negative_integers(self):
        self.assertEqual(self.calc.div(1, 2), 0.5)
        self.assertEqual(self.calc.div(2, 3), 0.667)
        self.assertEqual(self.calc.div(5, 4), 1.25)

    def test_div_double_negative_integers(self):
        result = self.calculator.div(-9, -3)
        self.assertEqual(result, 3)
        self.assertNotEqual(result, -3)

    def test_div_double_same_negative_integers(self):
        result = self.calculator.div(2, -2)
        self.assertEqual(result, -1)     

    def test_div_double_same_negative_integers(self):
        result = self.calculator.div(-3, -3)
        self.assertEqual(result, 1)
        self.assertNotEqual(result, -1)        

    def test_div_error(self):
        '''Make sure ZeroDivisionError is raised when necessary'''
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

if __name__ == '__main__':
    unittest.main()