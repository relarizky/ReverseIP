import requests
import pytest

from library.reverse.hacker_target import HackerTarget
from library.reverse.whois_xml import WhoisXML


@pytest.mark.factory
@pytest.mark.parametrize("factory", [HackerTarget, WhoisXML])
def test_factory_hacker_target(monkeypatch, mock_response, factory):

    # mock get and post method
    monkeypatch.setattr(requests, "get", mock_response)
    monkeypatch.setattr(requests, "post", mock_response)
    monkeypatch.setattr(requests.Session, "get", mock_response)
    monkeypatch.setattr(requests.Session, "post", mock_response)

    api = factory()
    site = api.reverse("target.com")

    assert site[0] == "Hello World"
