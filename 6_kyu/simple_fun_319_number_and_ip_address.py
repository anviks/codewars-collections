"""https://www.codewars.com/kata/5936371109ca68fe6900000c"""
from ipaddress import IPv4Address


def number_and_IP_address(s):
    if '.' in s:
        return str(int(IPv4Address(s)))
    return str(IPv4Address(int(s)))


def main():
    from util_funcs import pretty_compare

    pretty_compare(number_and_IP_address("10.0.3.193"), "167773121")
    pretty_compare(number_and_IP_address("167969729"), "10.3.3.193")


if __name__ == '__main__':
    main()
