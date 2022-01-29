import pytest
import requests

from library.api.hacker_target_api import HackerTargetAPI
from library.api.you_get_signal_api import YouGetSignalAPI

# i use parametrize in case you want to add more API classes that use
# the same GET or POST method for communcating with API endpoint

@pytest.mark.api
@pytest.mark.parametrize("api_obj_ref", [HackerTargetAPI])
def test_api_get_request(monkeypatch, mock_response, api_obj_ref):

    # mock text attribute of get class
    monkeypatch.setattr(requests, "get", mock_response)

    obj = api_obj_ref("target.com")
    obj.fetch()
    obj.scrap()

    assert obj.site[0] == "Hello World"


@pytest.mark.api
@pytest.mark.parametrize("api_obj_ref", [YouGetSignalAPI])
def test_api_post_request(monkeypatch, mock_response, api_obj_ref):

    # mock text attribute of get class

    assert True
