import unittest

from calculator import operations


class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(operations.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(operations.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(operations.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(operations.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            operations.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
