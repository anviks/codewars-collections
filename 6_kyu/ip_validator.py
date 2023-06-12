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
