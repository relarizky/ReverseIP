import os
import json

from typing import Union


def config_file_reader() -> dict:
    """CONFIG FILE READER

    function for reading config json file.

    Parameters
        None

    Returns
        content_json (dict): dictionary as result of parsed config nested json
    """

    FILE = os.getcwd() + "/.config.json"
    content_json = {}

    if os.path.isfile(FILE):
        with open(FILE, "r") as file:
            content = file.read()
            content_json = json.loads(content)

    return content_json


def result_saver(site_list: list, domain: str) -> None:
    """OBTAINED RESULT SAVER

    function for saving the obtained result into save/ directory
    """

    pass
