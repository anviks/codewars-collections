"""https://www.codewars.com/kata/541a354c39c5efa5fa001372"""
from ipaddress import IPv4Address


def ip_to_num(ip):
    return int(IPv4Address(ip))


def num_to_ip(num):
    return str(IPv4Address(num))


def main():
    from util_funcs import pretty_compare

    pretty_compare(ip_to_num('192.168.1.1'), 3232235777)
    pretty_compare(ip_to_num('10.0.0.0'), 167772160)
    pretty_compare(ip_to_num('176.16.0.1'), 2953838593)
    pretty_compare(ip_to_num('255.255.255.255'), 2 ** 32 - 1)
    pretty_compare(ip_to_num('0.0.0.0'), 0)
    pretty_compare(ip_to_num('0.152.13.172'), 9964972)

    pretty_compare(num_to_ip(3232235777), '192.168.1.1')
    pretty_compare(num_to_ip(167772160), '10.0.0.0')
    pretty_compare(num_to_ip(2953838593), '176.16.0.1')
    pretty_compare(num_to_ip(0), '0.0.0.0')
    pretty_compare(num_to_ip(2 ** 32 - 1), '255.255.255.255')
    pretty_compare(num_to_ip(9964972), '0.152.13.172')


if __name__ == '__main__':
    main()
