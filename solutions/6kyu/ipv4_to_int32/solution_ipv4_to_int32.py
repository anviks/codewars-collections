"""https://www.codewars.com/kata/52ea928a1ef5cfec800003ee"""

from ipaddress import IPv4Address


def ip_to_int32(ip):
    return int(IPv4Address(ip))
