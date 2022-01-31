import os
import pytest


class MockResponse:
    """class for mocking get and post classes"""

    text = "Hello World"
    status_code = 200

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def json(self):
        return {
            "result": [
                {"name": "Hello World"}
            ]
        }

class MockTextIOWrapper:
    """Class For Mocking Out TextIOWrapper"""

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def read(self):
        json = "{\"text\": \"Hello World\", "
        json = json + "\"app\": {\"save_dir\": \"/saved/\"}}"

        return json


@pytest.fixture
def mock_response():

    def response(*args, **kwargs):
        return MockResponse()

    return response


@pytest.fixture
def mock_open():

    def open_func(*args, **kwargs):
        return MockTextIOWrapper()

    return open_func


@pytest.fixture
def mock_isfile():

    def isfile(*args, **kwargs):
        return True

    return isfile
