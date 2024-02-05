#!/usr/bin/env python3
""" This module contains unit tests for GithubOrgClient class"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests GithubOrgClient class methods"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests GithubOrgClient.org"""
        url = f"https://api.github.com/orgs/{org_name}"
        github_client = GithubOrgClient(org_name)
        github_client.org()
        mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ("testing-url", {"repos_url": "https://example_url.com"})
    ])
    def test_public_repos_url(self, name, result):
        """Test GithubOrgClient._public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result["repos_url"])


if __name__ == '__main__':
    unittest.main()
