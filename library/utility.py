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


def result_saver(api_name: str, target: str, site_list: list) -> None:
    """OBTAINED RESULT SAVER

    function for saving the obtained result into save_dir.
    the file will be stored file with name that corresponds to
    API class name.

    Parameters
        api_name    (str): API Class Name
        target      (str): target domain or ip address
        site_list   (list): list of obtained sites

    Returns
        None
    """

    DIR = os.getcwd() + config_file_reader().get("app").get("save_dir")
    SUB_DIR = DIR + "/" + target + "/"

    def write_file(string: str) -> None:
        saving_file = SUB_DIR + api_name + ".txt"

        with open(saving_file, "a+") as file:
            file.write(string + "\n")

    if site_list != []:
        # prevent creating directory when the given site_list is empty
        if not os.path.isdir(SUB_DIR):
            # create saving_dir in case it does not exist
            os.makedirs(SUB_DIR, mode=0o777, exist_ok=True)

        for site in site_list:
            write_file(site)
