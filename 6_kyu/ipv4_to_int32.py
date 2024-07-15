"""https://www.codewars.com/kata/52ea928a1ef5cfec800003ee"""
from ipaddress import IPv4Address


def ip_to_int32(ip):
    return int(IPv4Address(ip))


def main():
    from util_funcs import pretty_compare

    pretty_compare(ip_to_int32("128.114.17.104"), 2154959208)
    pretty_compare(ip_to_int32("0.0.0.0"), 0)
    pretty_compare(ip_to_int32("128.32.10.1"), 2149583361)


if __name__ == '__main__':
    main()
