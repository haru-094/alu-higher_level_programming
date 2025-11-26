#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 1.5]), 1.5)

    def test_strings_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1000))), 999)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            max_integer("not a list")


if __name__ == "__main__":
    unittest.main()
