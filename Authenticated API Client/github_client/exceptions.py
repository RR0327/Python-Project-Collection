class GitHubClientError(Exception):
    """Base exception for GitHub client errors."""


class AuthenticationError(GitHubClientError):
    """Raised when authentication fails."""


class APIRequestError(GitHubClientError):
    """Raised for failed API requests."""
