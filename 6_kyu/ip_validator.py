"""
https://www.codewars.com/kata/515decfd9dcfc23bb6000006

**IP Validation**

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
    1.2.3.4\n
    123.45.67.89

Invalid input examples:
    1.2.3\n
    1.2.3.4.5\n
    123.456.78.90\n
    123.045.067.089

Notes:
    - Leading zeros (e.g. 01.02.03.04) are considered invalid
    - Inputs are guaranteed to be a single string
"""


def is_valid_IP(string: str):
    return len(octets := string.split(".")) == 4 and all((x.isdigit() and 0 <= int(x) <= 255 and (len(x) == 1 or x[0] != "0")) for x in octets)


def is_valid_IP_top_solution(string: str):
    import socket
    try:
        socket.inet_pton(socket.AF_INET, string)
        return True
    except socket.error:
        return False


if __name__ == '__main__':
    assert is_valid_IP("2.235a.2.2") is False
    assert is_valid_IP("2.True.2.2") is False
    assert is_valid_IP("2.2.02.2") is False
    assert is_valid_IP("192.168.1.1") is True
    assert is_valid_IP("0.0.0.0") is True
    assert is_valid_IP("0.1111.0.0") is False
    assert is_valid_IP("123.45.67.89") is True
