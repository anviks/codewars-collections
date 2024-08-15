"""https://www.codewars.com/kata/52e88b39ffb6ac53a400022e"""

from ipaddress import IPv4Address


def int32_to_ip(int32: int) -> str:
    return str(IPv4Address(int32))
