import unittest
from unittest.mock import patch, Mock

import github_client
from github_client import (
    calculate_average_stars,
    create_report,
    get_repos,
    get_top_repo,
)


class TestCalculateAverageStars(unittest.TestCase):
    def test_average_stars_for_repositories(self):
        filtered = [
            {"stargazers_count": 100},
            {"stargazers_count": 200},
            {"stargazers_count": 300}
        ]

        result = calculate_average_stars(filtered)

        self.assertEqual(result, 200)

    def test_average_stars_for_empty_list(self):
        filtered = []

        result = calculate_average_stars(filtered)

        self.assertEqual(result, 0)
class TestCreateReport(unittest.TestCase):
    def test_create_report(self):
        config = {
            "username": "octocat",
            "language": "Ruby"
        }

        repos = [
            {"stargazers_count": 100},
            {"stargazers_count": 200}
        ]

        filtered = [
            {"stargazers_count": 100}
        ]

        result = create_report(config, repos, filtered)

        expected = (
            "GitHub Repository Report\n"
            "User: octocat\n"
            "Total repositories: 2\n"
            "Filtered repositories: 1\n"
            "Average stars: 100.0\n"
            "Language filter: Ruby"
        )

        self.assertEqual(result, expected)

class TestGetTopRepo(unittest.TestCase):
    def test_get_top_repo(self):
        filtered = [
            {"name": "repo-a", "stargazers_count": 100},
            {"name": "repo-b", "stargazers_count": 500},
            {"name": "repo-c", "stargazers_count": 300}
        ]

        result = get_top_repo(filtered)

        expected = {
            "name": "repo-b",
            "stargazers_count": 500
        }

        self.assertEqual(result, expected)

    def test_get_top_repo_for_empty_list(self):
        result = get_top_repo([])

        self.assertIsNone(result)

class TestGetRepos(unittest.TestCase):
    @patch("github_client.requests.get")
    def test_get_repos_returns_fake_data(self, mock_get):
        fake_data = [
            {"name": "repo-a"},
            {"name": "repo-b"},
        ]

        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = fake_data
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = get_repos("octocat")

        self.assertEqual(result, fake_data)
        mock_get.assert_called_once()

    @patch("github_client.requests.get")
    def test_get_repos_returns_none_for_request_exception(self, mock_get):
        mock_get.side_effect = github_client.requests.RequestException(
            "Network error"
        )

        result = get_repos("octocat")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
