#!/usr/bin/env python3
""" a module to test utils """
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


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

    @parameterized.expand([({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test raising errors if params are not right"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""

    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


unittest.main()
