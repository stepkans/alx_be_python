import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    """Set up the SimpleCalculator instance before each test."""
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(-5, 2), -3)
        self.assertEqual(self.calc.add(-2, -2), -4)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self): 
        """Test the subtraction method.""" 
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-5, 2), -7)
        self.assertEqual(self.calc.subtract(-2, -2), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)  

    def test_multiplication(self):  
        """Test the multiplication method.""" 
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(-5, 2), -10)
        self.assertEqual(self.calc.multiply(-2, -2), 4)     
        self.assertEqual(self.calc.multiply(10, 0), 0)     

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-5, 2), -2.5)
        self.assertEqual(self.calc.divide(-2, -2), 1)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertIsNone(self.calc.divide(5, 0))
           


if __name__ == "__main__":
    unittest.main()
