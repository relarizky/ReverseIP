from library.api.base import APIScrapper
from library.api.whois_xml_api import WhoisXMLAPI
from library.reverse.base import ReverseIP


class WhoisXML(ReverseIP):
    """Class for performing Reverse IP / Domain with WhoisXML API

    Parameters
        None

    Returns
        object  (WhoisXML)

    Example
        >>> x = WhoisXML()
        >>> y = x.reverse("target.com")
        >>> print(y)
        ['target.com', 'other.com']
    """

    def create_api(self, *args, **kwargs) -> APIScrapper:
        return WhoisXMLAPI(*args, **kwargs)
