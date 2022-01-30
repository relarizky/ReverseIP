import pytest
import builtins

from library.utility import config_file_reader


class MockTextIOWrapper:
    """Class For Mocking Out TextIOWrapper"""

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def read(self):
        return "{\"text\": \"Hello World\"}"


@pytest.mark.utility
def test_config_file_reader(monkeypatch):

    def mock_open(*args, **kwargs):
        return MockTextIOWrapper()

    # mock out the open builtin func to avoid real file reading
    with monkeypatch.context() as mock:
        mock.setattr(builtins, "open", mock_open)
        api_key = config_file_reader()

    assert api_key.get("text") == "Hello World"


@pytest.mark.utility
def test_result_saver(monkeypatch):

    assert True
