#!/usr/bin/env python3
""" This module contains unit tests for GithubOrgClient class"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import json


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

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mocked_method, mocked_public):
        """ test public_repos """
        payload = [{"name": "repo1"}, {"name": "repo2"}]
        mocked_method.return_value = payload

        mocked_public.return_value = "https://example_url.com/repos"
        github_client = GithubOrgClient("testorg")

        result = github_client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])

        mocked_public.assert_called_once()
        mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected_result):
        """test has_license"""
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expected_result)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test: fixtures """
    @classmethod
    def setUpClass(cls):
        """setupclass"""
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public repos """
        github_client = GithubOrgClient("testorg")
        result = github_client.public_repos()

        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """test public with license"""
        github_client = GithubOrgClient("testorg")
        result = github_client.public_repos(license="apache-2.0")

        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
