from calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def setUp(self):  # in unit tests, we create instance variables in setUp function.
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4, 5), 9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, -4), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(25, 5), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)


if __name__ == "__main__":
    unittest.main()
