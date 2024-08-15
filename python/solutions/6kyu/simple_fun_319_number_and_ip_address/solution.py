"""https://www.codewars.com/kata/5936371109ca68fe6900000c"""

from ipaddress import IPv4Address


def number_and_IP_address(s):
    if '.' in s:
        return str(int(IPv4Address(s)))
    return str(IPv4Address(int(s)))
