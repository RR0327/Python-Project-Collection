from typing import Dict, Any
import httpx

from .exceptions import AuthenticationError, APIRequestError
from .logger import get_logger


class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self, token: str) -> None:
        self.token = token
        self.logger = get_logger(self.__class__.__name__)

        self.headers: Dict[str, str] = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
        }

    def _get(self, endpoint: str) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = httpx.get(url, headers=self.headers, timeout=10)

            if response.status_code == 401:
                self.logger.error("Authentication failed")
                raise AuthenticationError("Invalid GitHub token")

            if response.status_code != 200:
                self.logger.error(
                    "Request failed | Status: %s | Body: %s",
                    response.status_code,
                    response.text,
                )
                raise APIRequestError("GitHub API request failed")

            return response.json()

        except httpx.RequestError as exc:
            self.logger.exception("Network error occurred")
            raise APIRequestError("Network error") from exc

    def get_user(self, username: str) -> Dict[str, Any]:
        return self._get(f"/users/{username}")
