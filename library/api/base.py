from __future__ import annotations
from abc import ABC, abstractmethod


class APIScrapper(ABC):
    """API Scrapper Base Class
    inherit this class if you want to create new class for scrapping
    your new API resource.
    """

    @abstractmethod
    def fetch(self) -> None:
        """create request to the given API endpoint and fetch data"""

        pass

    @abstractmethod
    def scrap(self) -> list:
        """scrap the website list from the fetched data"""

        pass

    @property
    @abstractmethod
    def site(self) -> list:
        """property that refers to resulting site lists"""

        pass
