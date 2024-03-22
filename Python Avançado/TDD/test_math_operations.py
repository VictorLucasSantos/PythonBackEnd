import unittest

from TDD.math_operations import addition_operation, subtraction_operation


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        math_addition = addition_operation(num_1=1, num_2=2)
        self.assertEqual(math_addition, 3)

    def test_subtraction(self):
        math_addition = subtraction_operation(num_1=10, num_2=10)
        self.assertEqual(math_addition, 15)


if __name__ == '__main__':
    unittest.main()
