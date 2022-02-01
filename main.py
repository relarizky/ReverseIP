import sys
import time

from library.utility import result_saver
from library.reverse.whois_xml import WhoisXML
from library.reverse.hacker_target import HackerTarget


def reverse_ip(option: int, target: str, displayed: bool = False) -> None:
    """Use Reverse IP Classes to Perform Reverse IP

    Parameters
        option   (int): option number that refers to the existing api
        target   (str): target ip address or domain
        diplayed (bool): display the result or not (default: False)

    Returns
        None
    """

    if option == 1:
        tools = [WhoisXML()]
    elif option == 2:
        tools = [HackerTarget()]
    elif option == 3:
        tools = [WhoisXML(), HackerTarget()]

    for tool in tools:
        name = type(tool).__name__
        sites = tool.reverse(target)
        print(f"[+] {name} ({str(len(sites))})")
        result_saver(name, target, sites)
        time.sleep(0.45)
        if displayed:
            for site in sites:
                print(f"[+] {site}")


def banner() -> None:
    print(" _____                              _____ _____")
    print("|  __ \                            |_   _|  __ \\")
    print("| |__) |_____   _____ _ __ ___  ___  | | | |__) |")
    print("|  _  // _ \ \ / / _ \ '__/ __|/ _ \ | | |  ___/")
    print("| | \ \  __/\ V /  __/ |  \__ \  __/_| |_| |")
    print("|_|  \_\___| \_/ \___|_|  |___/\___|_____|_|")
    print("--------------------------------------------")


def main() -> None:

    target = sys.argv[1]
    displayed = True if len(sys.argv) == 3 and sys.argv[2] == "yes" else None

    try:
        print("[1] WhoisXML")
        print("[2] Hacker Target")
        print("[3] All")
        print("[>] ", end="")
        option = int(input())
    except ValueError:
        print("[-] Only accept number input!")
    except KeyboardInterrupt:
        exit(0)

    reverse_ip(option, target, displayed)


if __name__ == "__main__":

    banner()
    if not (1 < len(sys.argv) <= 3):
        print(f"[+] Usage: python3 {sys.argv[0]} target.com yes")
        exit(0)

    main()
