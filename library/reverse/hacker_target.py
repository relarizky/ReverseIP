from sys import exit
from library.api.base import APIScrapper
from library.api.hacker_target_api import HackerTargetAPI
from library.reverse.base import ReverseIP
from library.utility import config_file_reader


class HackerTarget(ReverseIP):
    """Class for performing Reverse IP/Domain with HackerTarget API

    Parameters
        None

    Returns
        object  (HackerTarget)

    Example
        >>> x = HackerTarget()
        >>> y = x.reverse("target.com")
        >>> print(y)
        ['target.com', 'other.com']
    """

    def create_api(self, *args, **kwargs) -> APIScrapper:
        return HackerTargetAPI(*args, **kwargs)

    def reverse(self, *args, **kwargs) -> None:
        target = args[0] or kwargs["target"]
        config = config_file_reader().get("api")
        page = config.get("HackerTarget").get("page") if config else None
        key = config.get("HackerTarget").get("page") if config else None

        try:
            api = self.create_api(target=target, page=page, key=key)
            api.fetch()
            api.scrap()
        except Exception:
            print("Seems like you have bad connection or invalid input")
            exit(0)

        return api.site
