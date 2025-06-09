
import unittest

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test case
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition method"""
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)

    def test_multiply(self):
        """test multiply method"""
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_subtraction(Self):
        """test subtraction"""
        Self.assertEqual(Self.calc.subtract(2,2), 0)
  

    def test_divide(self):
        """test divide"""
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_by_zero(self):
        """test divide by zero"""
        with self.assertRaises(ZeroDivisionError):
            result = 1/0

