#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_max_at_end(self):
        """Test when max is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when max is in the middle of the list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative_number(self):
        """Test with one negative number in the list"""
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_only_negative_numbers(self):
        """Test with only negative numbers in the list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_one_element(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed_integers(self):
        """Test with mixed positive and negative integers"""
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_numbers(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([-1, 0, 1.5]), 1.5)

    def test_list_with_duplicates(self):
        """Test with duplicate values"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_large_list(self):
        """Test with a large list"""
        self.assertEqual(max_integer(list(range(1000))), 999)

    def test_no_arguments(self):
        """Test with no arguments (default empty list)"""
        self.assertIsNone(max_integer())


if __name__ == "__main__":
    unittest.main()
