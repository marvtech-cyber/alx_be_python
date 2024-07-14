import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(10, 0), None)

if __name__ == "__main__":
    unittest.main()
