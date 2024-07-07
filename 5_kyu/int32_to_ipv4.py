"""https://www.codewars.com/kata/52e88b39ffb6ac53a400022e"""
from ipaddress import IPv4Address


def int32_to_ip(int32: int) -> str:
    return str(IPv4Address(int32))


def main():
    from util_funcs import pretty_compare

    pretty_compare(int32_to_ip(2154959208), "128.114.17.104")
    pretty_compare(int32_to_ip(0), "0.0.0.0")
    pretty_compare(int32_to_ip(2149583361), "128.32.10.1")


if __name__ == '__main__':
    main()
