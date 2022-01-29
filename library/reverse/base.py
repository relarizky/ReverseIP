from __future__ import annotations
from abc import ABC, abstractmethod


class ReverseIP(ABC):

    @abstractmethod
    @staticmethod
    def create_rip():
        """return API object"""

        pass

    def reverse_ip() -> list:
        """start connect to API"""

        rip = self.create_rip()
        rip.reverse()

        return rip.site_list
