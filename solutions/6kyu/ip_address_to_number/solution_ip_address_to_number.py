"""https://www.codewars.com/kata/541a354c39c5efa5fa001372"""

from ipaddress import IPv4Address


def ip_to_num(ip):
    return int(IPv4Address(ip))


def num_to_ip(num):
    return str(IPv4Address(num))
