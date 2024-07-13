import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    """Set up the SimpleCalculator instance before each test."""
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(-5, 2), -3)
        self.assertEqual(self.calc.add(-2, -2), -4)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self): 
        """Test the subtract method.""" 
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(-5, 2), -7)
        self.assertEqual(self.calculator.subtract(-2, -2), 0)
        self.assertEqual(self.calculator.subtract(5, 0), 5)  

    def test_multiply(self):  
        """Test the multiply method.""" 
        self.assertEqual(self.calculator.multiply(5, 2), 10)
        self.assertEqual(self.calculator.multiply(-5, 2), -10)
        self.assertEqual(self.calculator.multiply(-2, -2), 4)     
        self.assertEqual(self.calculator.multiply(10, 0), 0)     

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        self.assertEqual(self.calculator.divide(-5, 2), -2.5)
        self.assertEqual(self.calculator.divide(-2, -2), 1)
        self.assertEqual(self.calculator.divide(0, 1), 0)
        self.assertIsNone(self.calculator.divide(5, 0))
