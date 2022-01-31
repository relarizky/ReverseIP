import pytest
import requests

from library.api.whois_xml_api import WhoisXMLAPI
from library.api.hacker_target_api import HackerTargetAPI

@pytest.mark.api
def test_api_hacker_target(monkeypatch, mock_response):

    # mock text attribute of get class
    monkeypatch.setattr(requests, "get", mock_response)

    obj = HackerTargetAPI("target.com")
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
