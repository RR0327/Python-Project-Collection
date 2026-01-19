import pytest
from github_client.client import GitHubClient
from github_client.exceptions import AuthenticationError, APIRequestError


class MockResponse:
    def __init__(self, status_code, json_data=None, text=""):
        self.status_code = status_code
        self._json = json_data or {}
        self.text = text

    def json(self):
        return self._json


def test_get_user_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(200, {"login": "octocat"})

    monkeypatch.setattr("httpx.get", mock_get)

    client = GitHubClient("fake-token")
    data = client.get_user("octocat")

    assert data["login"] == "octocat"


def test_authentication_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(401)

    monkeypatch.setattr("httpx.get", mock_get)

    client = GitHubClient("bad-token")

    with pytest.raises(AuthenticationError):
        client.get_user("octocat")


def test_api_failure(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(500, text="Server error")

    monkeypatch.setattr("httpx.get", mock_get)

    client = GitHubClient("token")

    with pytest.raises(APIRequestError):
        client.get_user("octocat")
