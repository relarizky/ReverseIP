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

## Usage
```
 _____                              _____ _____
|  __ \                            |_   _|  __ \
| |__) |_____   _____ _ __ ___  ___  | | | |__) |
|  _  // _ \ \ / / _ \ '__/ __|/ _ \ | | |  ___/
| | \ \  __/\ V /  __/ |  \__ \  __/_| |_| |
|_|  \_\___| \_/ \___|_|  |___/\___|_____|_|
--------------------------------------------
[+] Usage: python3 main.py target.com yes
```

all the found results will be automatically stored in __saved/<yourtarget.com>/__ directory .

## Preview
<center><img src="https://github.com/relarizky/reverse-ip/blob/master/screenshot/preview.png?raw=true" height=20% width=50%></center>

## Notes
__.config.json__ is configuration file that is used for storing information like API key or default result saving directory.<br>
if you create new API and ReverseIP class, store your API information in __.config.json__<br>
then call the stored information inside reverse() method in your ReverseIP class.<br>
Looking at HackerTarget class will give you a guide.

## To do
 - Add more APIs
 - Make it colorful

## Contribution
any contribution will be really appreciated.

## License
This software is licensed under MIT License.
