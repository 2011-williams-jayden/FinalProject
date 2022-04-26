#Test Driver: Division Testing
#Date: 4/26/22
#Author: Jayden Williams

import unittest

class Calculator:
    def __init__(self):
        pass

    def div(self, a, b):
        if b != 0:
            return a / b

class TestCalcDiv(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator()

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

#unittest.main(argv=[''], defaultTest='TestCalcDiv', verbosity=2, exit=False)

if __name__ == '__main__':
    unittest.main()