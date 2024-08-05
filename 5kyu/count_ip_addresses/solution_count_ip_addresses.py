"""https://www.codewars.com/kata/526989a41034285187000de4"""

from ipaddress import IPv4Address


def ips_between(start: str, end: str) -> int:
    return int(IPv4Address(end)) - int(IPv4Address(start))
