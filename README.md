# ReverseIP

![https://img.shields.io/github/license/relarizky/reverse-ip](https://img.shields.io/github/license/relarizky/reverse-ip)
![https://img.shields.io/badge/python-3.8.10-blue](https://img.shields.io/badge/python-3.8.10-blue)

Python-based script for performing Reverse IP on your penetration testing target. <br>
This tool uses external APIs to do so, and you can add more APIs that you know to richify your result. <br>
This tool is also built with good design that's very recognizable and understandable so you can add more APIs with ease.

## Installation
```
$ git clone https://github.com/relarizky/reverse-ip
$ cd reverse-ip/
$ pip install requests pytest
$ python main.py
```

## Preview
<center><img src="https://github.com/relarizky/reverse-ip/blob/master/screenshot/preview.png?raw=true" height=20% width=50%></center>

## Notes
__.config.json__ is configuration file that is used for storing information like API key or default result saving directory.<br>
if you create new API and ReverseIP class, store your API information in __.config.json__<br>
then call the stored information inside reverse() method in your ReverseIP class.<br>
Looking at HackerTarget class will give you a guide.

## Contribution
any contribution will be really appreciated.

## License
This software is licensed under MIT License.
