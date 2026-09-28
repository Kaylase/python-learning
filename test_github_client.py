import unittest

from github_client import calculate_average_stars, create_report, get_top_repo


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


if __name__ == "__main__":
    unittest.main()
