import pytest


class MockResponse:
    """class for mocking get and post classes"""

    text = "Hello World"

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass


@pytest.fixture
def mock_response():

    def response(*args, **kwargs):
        return MockResponse()

    return response
