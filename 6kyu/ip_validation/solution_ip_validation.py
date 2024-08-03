"""https://www.codewars.com/kata/515decfd9dcfc23bb6000006"""


def is_valid_IP(string: str):
    return len(octets := string.split(".")) == 4 and all(
        (x.isdigit() and 0 <= int(x) <= 255 and (len(x) == 1 or x[0] != "0")) for x in octets)


def is_valid_IP_top_solution(string: str):
    import socket
    try:
        socket.inet_pton(socket.AF_INET, string)
        return True
    except socket.error:
        return False
