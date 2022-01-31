from __future__ import annotations
from abc import ABC, abstractmethod
from sys import exit
from library.api.base import APIScrapper


class ReverseIP(ABC):
    """ReverseIP Base Class

    this is the interface or factory of API classes.
    if you already created new API class, create new class that
    derives from this class to use your API class.
    """

    @abstractmethod
    def create_api(self, *args, **kwargs) -> APIScrapper:
        """create API object

        Parameters
            this method accepts any inputs

        Returns
            object  (APIScrapper)
        """

        pass

    def reverse(self, *args, **kwargs) -> list:
        """start performing reverse ip / domain

        Parameters
            this method accepts any inputs

        Returns
            site_list   (list): list of sites as result of reverse ip / domain
        """

        try:
            api = self.create_api(*args, **kwargs)
            api.fetch()
            api.scrap()
        except Exception:
            print("Seems like you have bad connection or invalid input.")
            exit(0)

        return api.site
