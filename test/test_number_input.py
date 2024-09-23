"""SQL Injection Validator tests"""
import unittest

from src.inputs import number_input

input_list = [
    "4.08E+10",
    "abc",
    "123abc",
    "abc123",
    "$1234",
    "12,34",
    "12/34",
    "12-34",
    "12 34",
    "12:34",
    "12;34",
    False,
    True,
    None
]


class TestNumberValidator(unittest.TestCase):
    """Number Validator test cases"""

    def test_number_input_with_valid_data(self):
        """Test number_input with valid data"""
        self.assertTrue(number_input(500))

    def test_number_input_with_invalid_data(self):
        """Test invalid number_input"""
        for input_test in input_list:
            with self.assertRaises(ValueError):
                number_input(input_test)


if __name__ == '__main__':
    unittest.main()
