"""https://www.codewars.com/kata/57814d79a56c88e3e0000786"""


def decrypt(encrypted_text, n):
    is_odd_length = len(encrypted_text) % 2

    for _ in range(n):
        half_length = len(encrypted_text) // 2
        pairs = zip(encrypted_text[half_length:], encrypted_text[:half_length] + '\0')
        encrypted_text = ''.join(''.join(pair) for pair in pairs)
        if is_odd_length:
            encrypted_text = encrypted_text[:-1]

    return encrypted_text


def encrypt(text, n):
    for _ in range(n):
        text = text[1::2] + text[::2]
    return text
