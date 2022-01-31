import re
import socket
import requests

from library.api.base import APIScrapper


class WhoisXMLAPI(APIScrapper):
    """Scrapper For Whois XML API

    for performing reverse ip address through WhoisXML API
    this class will be used in ReverseIP Classes.

    Parameters
        target  (str): target domain or ip address

    Returns
        object  (WhoisXMLAPI)

    Example
        >>> x = WhoisXMLAPI("target.com")
        >>> x.fetch()
        >>> x.scrap()
        >>> print(x.site)
        ['target.com', 'other.com']
    """

    SITE = "https://dns-history.whoisxmlapi.com/"

    def __init__(
        self,
        target: str
    ) -> None:
        self.target = socket.gethostbyname(target)
        self.json = {}
        self.request = requests.Session()   # for persisting the given cookie
        self.site_list = []
        self.csrf_token = None  # required for every request to API endpoint

    # create static method for crafting post data
    # to shorten the row required for crafting it :P
    # im just trying to keep the code clean :D
    @staticmethod
    def _craft_post_data(target: str) -> dict:
        """Craft the required post data

        Parameters
            target  (str): target ip address

        Returns
            data    (dict): required post data
        """

        data = {}
        data.update({"search": target})
        data.update({"web-lookup-search": True})
        data.update({"g-recaptcha-response": None})

        return data

    # again, it's just for shortening the row :D
    def _craft_headers(self) -> dict:
        """Craft the required header"""

        header = {}
        header.update({"User-Agent": "Opera/9.60 (Windows NT 6.0) Presto/2.1.1"})
        header.update({"Referer": "https://dns-history.whoisxmlapi.com/"})
        header.update({"X-Requested-With": "XMLHttpRequest"})
        header.update({"X-Csrf-Token": self.csrf_token})
        header.update({"Origin": "https://dns-history.whoisxmlapi.com"})

        return header

    def _fetch_csrf_token(self):
        """Fetch CSRF-TOKEN required for request"""

        url =  self.SITE
        regex = r"\<meta name\=\"csrf-token\" content=\"(.*?)\"\>"

        with self.request.get(url=url, allow_redirects=False) as request:
            response = request.text
            token = re.findall(regex, response)

        self.csrf_token = token[0] if token else None

    def fetch(self) -> None:
        self._fetch_csrf_token()
        url = self.SITE + "api/web"
        data = self._craft_post_data(self.target)
        headers = self._craft_headers()

        with self.request.post(url, json=data, headers=headers) as request:
            if request.status_code == 200:
                self.json = request.json()

    def scrap(self) -> None:
        json = self.json
        if len(json) != 0:
            site_list = [result.get("name") for result in json.get("result")]
            self.site_list = site_list
        else:
            self.site_list = []

    @property
    def site(self) -> list:
        return self.site_list
