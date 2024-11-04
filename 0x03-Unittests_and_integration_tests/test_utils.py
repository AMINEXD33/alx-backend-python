#!/usr/bin/env python3
""" a module to test utils """
from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """
    A test case for nested Map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """test accessing a nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
            [
                ({}, ("a",), KeyError),
                ({"a": 1}, ("a", "b"), KeyError)
            ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test raising errors"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


unittest.main()