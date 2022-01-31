import os
import builtins
import pytest
import library.utility


@pytest.mark.utility
def test_config_file_reader(monkeypatch, mock_open, mock_isfile):

    # mock out the open() and os.path.isfile() builtin func to avoid real file reading
    with monkeypatch.context() as mock:
        mock.setattr(os.path, "isfile", mock_isfile)
        mock.setattr(builtins, "open", mock_open)
        api_key = library.utility.config_file_reader()

    assert api_key.get("text") == "Hello World"


@pytest.mark.utility
def test_result_saver(monkeypatch, tmp_path):

    def read_temp_file(file_name: str) -> list:
        with open(file_name, "r") as file:
            content = file.readlines()

        return list(map(lambda site: site.strip(), content))

    def mock_config_file_reader():
        return {"app": {"save_dir": "/saved/"}}

    with monkeypatch.context() as mock:
        # mock out os.getcwd() func to avoding create real directory
        mock.setattr(os, "getcwd", lambda *args: str(tmp_path))
        mock.setattr(
            library.utility,
            "config_file_reader",
            mock_config_file_reader
        )

        # api 1
        domain1 = "test.com"
        api_name1 = "HackerTarget"
        site_list1 = ["test.test.com", "tes.test.com"]

        # api 2
        domain2 = "test.com"
        api_name2 = "YouGetSignal"
        site_list2 = ["test.test.com", "tes.test.com"]

        # these following variables define temporary resources
        dirs = str(tmp_path) + library.utility.config_file_reader().get("app").get("save_dir")
        file1 = dirs + domain1 + "/" + api_name1 + ".txt"
        file2 = dirs + domain2 + "/" + api_name2 + ".txt"

        library.utility.result_saver(api_name1, domain1, site_list1)
        library.utility.result_saver(api_name2, domain2, site_list2)

    assert os.listdir(dirs) == ["test.com"]
    assert os.listdir(dirs + "test.com") == [api_name1+".txt", api_name2+".txt"]
    assert read_temp_file(file1) == site_list1
    assert read_temp_file(file2) == site_list2
