import requests

from library.api.base import APIScrapper


class HackerTargetAPI(APIScrapper):
    """Scrapper For Hacker Target API

    for performing reverse ip address through hacker target API
    this class will be used in ReverseIP classes.

    Parameters
        target  (str): target domain or ip address
        page    (int): total page
        key     (str): api key for hacker target api

    Returns
        object  (HackerTargetAPI)

    Example
        >>> x = HackerTargetAPI("target.com")
        >>> x.fetch()
        >>> x.scrap()
        >>> print(x.site)
        ['target.com', 'other.com']
    """

    END_POINT = "https://api.hackertarget.com/reverseiplookup/"

    def __init__(
        self,
        target: str,
        page: int = None,
        key: str = None
    ) -> None:
        self.key = key
        self.page = page
        self.text = ""
        self.target = target
        self.site_list = []

    @staticmethod
    def __define_parameter(target: str, page: int, key: str) -> dict:
        """Define required parameter for request

        Parameters
            target (str): target domain or ip address
            page   (int): page total
            key    (str): api key of hacker target

        Returns
            parameter (dict): required paramater for requests

        Example
            >>> y = HackerTargetAPI.__define_paramter("target.com", 1, "xxx")
            >>> print(y)
            {'q': 'target.com', 'page': 1, 'apikey': 'xxx'}
        """

        parameter = {}
        parameter.update({"q": target})
        parameter.update({"page": page} if page is not None else {})
        parameter.update({"apikey": key} if key is not None else {})

        return parameter

    def fetch(self) -> None:
        url = self.END_POINT
        params = self.__define_parameter(self.target, self.page, self.key)
        headers = {"User-Agent": "Googlebot/2.1"}

        with requests.get(url=url, headers=headers, params=params) as req:
            # auto close the connection
            if req.status_code == 200:
                self.text = req.text

    def scrap(self) -> None:
        response = self.text
        site_list = filter(lambda site: site != "", response.split("\n"))
        self.site_list = list(site_list)

    @property
    def site(self) -> list:
        return self.site_list
