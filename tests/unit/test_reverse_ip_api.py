import pytest
import requests

from library.api.whois_xml_api import WhoisXMLAPI
from library.api.hacker_target_api import HackerTargetAPI

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
def test_api_whois_xml(monkeypatch, mock_response):

    # mock text attribute of post class
    monkeypatch.setattr(requests.Session, "get", mock_response)
    monkeypatch.setattr(requests.Session, "post", mock_response)

    obj = WhoisXMLAPI("target.com")
    obj.fetch()
    obj.scrap()

    assert obj.site[0] == "Hello World"
