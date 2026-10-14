import unittest

from deepfake import add, subtract, multiply, divide, power, sqrt, percent


class CalculatorTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(divide(9, 3), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_advanced(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(percent(200, 10), 20)


if __name__ == "__main__":
    unittest.main()
