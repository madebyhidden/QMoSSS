import unittest
import requests

BASE_URL = "https://api.github.com/repos/BaFon77/TeaProjectFrontend"


class TestSC24Repo(unittest.TestCase):

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
        self.assertGreaterEqual(repo_data["created_at"], "2024-02-29T10:06:50Z")

    def test_repo_not_archived(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("archived", repo_data)
        self.assertFalse(repo_data["archived"])

    def test_repo_has_license(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("license", repo_data)
        self.assertIn("name", repo_data["license"])
        self.assertEqual(repo_data["license"]["name"], "MIT License")

    def test_repo_has_topics(self):
        response = requests.get(BASE_URL)
        repo_data = response.json()
        self.assertIn("topics", repo_data)
        self.assertIsInstance(repo_data["topics"], list)
        self.assertEqual(len(repo_data["topics"]), 0)  # Assuming topics list is empty

if __name__ == '__main__':
    unittest.main()
