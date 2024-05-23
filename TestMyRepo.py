import unittest
import requests

BASE_URL = "https://api.github.com/repos/madebyhidden/DPV_FA"


class TestGitHubMyRepo(unittest.TestCase):

    def test_repo_exists(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_repo_language(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("language", repo_data)
        self.assertEqual(repo_data["language"], "Java")

    def test_repo_has_issues(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("has_issues", repo_data)
        self.assertTrue(repo_data["has_issues"])

    def test_repo_has_wiki(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("has_wiki", repo_data)
        self.assertTrue(repo_data["has_wiki"])

    def test_repo_created_recently(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("created_at", repo_data)
        self.assertGreaterEqual(repo_data["created_at"], "2023-12-03T10:17:27Z")

    def test_repo_not_archived(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("archived", repo_data)
        self.assertFalse(repo_data["archived"])


if __name__ == '__main__':
    unittest.main()
