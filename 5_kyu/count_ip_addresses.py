"""https://www.codewars.com/kata/526989a41034285187000de4"""
from ipaddress import IPv4Address


def ips_between(start: str, end: str) -> int:
    return int(IPv4Address(end)) - int(IPv4Address(start))


def main():
    from util_funcs import pretty_compare

    pretty_compare(ips_between("150.0.0.0", "150.0.0.1"), 1)
    pretty_compare(ips_between("10.0.0.0", "10.0.0.50"), 50)
    pretty_compare(ips_between("20.0.0.10", "20.0.1.0"), 246)
    pretty_compare(ips_between("10.11.12.13", "10.11.13.0"), 243)
    pretty_compare(ips_between("160.0.0.0", "160.0.1.0"), 256)


if __name__ == '__main__':
    main()
