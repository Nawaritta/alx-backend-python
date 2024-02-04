#!/usr/bin/env python3
""" This module contains unit tests for utils"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """tests the method return """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """tests if a KeyError is raised in case we have an exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests if utils.get_json returns the expected result"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """Sets up the mock object and its json method"""

        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)

        mock_requests_get.stop()


class TestMemoize(unittest.TestCase):
    """ Tests utils.memoize decorator """

    def test_memoize(self):
        """ memoize test method """

        class TestClass:
            """TestClass"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            test_instance = TestClass()
            test_instance.a_property
            test_instance.a_property
            mocked.assert_called_once()
