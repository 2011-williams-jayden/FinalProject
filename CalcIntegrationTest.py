#Test Driver: Addition Testing
#Date: 4/26/22
#Author: Jayden Williams

import unittest
import Calculator

class TestCalc(unittest.Calculator):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator()

    def test_sub_add(self):
        self.assertEqual(self.calc.sub(15, 5), 10)
        self.assertEqual(self.calc.add(7, 2), 9)

    def test_mult_div(self):
        self.assertEqual(self.calc.mul(5, 5), 25)
        self.assertEqual(self.calc.add(30, 2), 15)

    def test_user_input(self):
        self.assertEqual(self.calc.input('3')('3'))
        self.assertEqual(self.calc.input('4')('4'))
        
    def test_input_divfunction(self):
        self.assertEqual(self.calc.input('4')('4'))
        self.assertEqual(self.calc.div(20, 5), 4)
        
    def test_input_addfunction(self):
        self.assertEqual(self.calc.input('1')('1'))
        self.assertEqual(self.calc.add(3, 5), 8)
        
    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

if __name__ == '__main__':
    unittest.main()
