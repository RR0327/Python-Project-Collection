# Explanation

This project is a professional-grade **Python API Client Wrapper** for GitHub. It follows industry standards by separating concerns into logging, error handling, networking, and testing.

1. **Custom Exceptions (exceptions.py)**

   This file defines a hierarchy of errors. Custom exceptions make your code more readable and allow users to catch specific issues (like a bad token) separately from general network failures.

- _class GitHubClientError(Exception)::_ The "Parent" exception. Catching this will catch any error related to this library.

- _class AuthenticationError(GitHubClientError)::_ Specifically for 401 Unauthorized responses (invalid/expired tokens).

- _class APIRequestError(GitHubClientError)::_ For general API issues, such as 404 Not Found or 500 Server Error.

2. **Centralized Logger (logger.py)**

   This utility ensures that every part of the application logs information consistently to a file.

- _logger = logging.getLogger(name):_ Creates a logger instance. Using **name** helps identify which file triggered the log.

- _logger.setLevel(logging.INFO):_ Sets the threshold; it will record "INFO", "WARNING", and "ERROR" messages.

- _handler = logging.FileHandler("github_client.log"):_ Tells the script to save logs into a physical file named github_client.log.

- _formatter = logging.Formatter(...):_ Defines the look of the log (Timestamp | Level | Name | Message).

3. **Authenticated API Client (client.py)**

   This is the "Engine" of the project. It handles the communication with GitHub.

- _BASE_URL = "https://api.github.com":_ The standard entry point for all GitHub API requests.

- _def **init**(self, token: str):_ When you create a client, you provide your personal access token.

- _self.headers:_ Sets up the required HTTP headers, including the Bearer Token for identity and the Accept header to specify the API version.

- _def \_get(self, endpoint: str):_ A private method (indicated by the \_). It contains the logic for sending requests and handling common HTTP errors.

- _response = httpx.get(...):_ Uses the **httpx** library to send the request with a 10-second timeout to prevent the script from hanging forever.

- _if response.status_code == 401:_ Checks if the token is valid; if not, it logs the error and raises our custom **AuthenticationError**.

- _return response.json():_ If everything is successful (200 OK), it converts the raw data into a Python dictionary.

- _get_user(self, username):_ A "Public" helper method that makes fetching a specific user as easy as calling **client.get_user("octocat")**.

4. **Package Init (**init**.py)**

   This file makes the folder a Python package and simplifies imports for the user.

- _from .client import GitHubClient:_ Allows a user to type **from github_client import GitHubClient** instead of the longer **from github_client.client import GitHubClient.**

- **all** = ["GitHubClient"]: Explicitly defines what is exported when someone uses **from github_client import \***.

5. **Unit Tests (tests/test_client.py)**

   These ensure the code works without actually hitting GitHub's servers (which is faster and avoids rate limits).

- _class MockResponse:_ A "fake" version of the **httpx** response object used to simulate different scenarios (Success, 401 Error, 500 Error).

- _monkeypatch.setattr("httpx.get", mock_get):_ This "tricks" the code. When **client.py** calls **httpx.get**, it actually runs our **mock_get** function instead.

- _test_get_user_success:_ Verifies that if the API returns code 200, our client correctly parses the username.

- _with pytest.raises(AuthenticationError):_ A test that passes only if the code correctly identifies a bad token and throws the right error.

6. **Project Configuration (pyproject.toml)**

- _addopts = "--cov=github_client --cov-report=term-missing":_ This tells **pytest** to automatically calculate Code Coverage. It shows you exactly which lines of your code were tested and which ones were missed.

  **How the Code Works (The Flow)**

1. **Initialization:** You create a GitHubClient with a token.

2. **Request:** You call get_user("octocat").

3. **Internal Processing:** The client builds the URL, attaches your token, and sends it via **httpx**.

4. **Safety Check:** If the internet is down or the token is bad, the **\_get** method catches the error, writes it to **github_client.log**, and alerts you via a Custom Exception.

5. **Result:** If successful, you get a clean Python dictionary containing the user's GitHub profile data.
