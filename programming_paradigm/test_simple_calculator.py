import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()
    def test_add(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(result, 4)

    def test_division(self):
        result = self.calc.divide(4, 2)
        self.assertEqual(result, 2)

    def test_zero_division(self):
        result = self.calc.divide(10, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()
