"""https://www.codewars.com/kata/simple-encryption-number-4-qwerty"""


def encrypt(text: str, encrypt_key: int):
    return shift_string(text, (encrypt_key // 100, encrypt_key // 10 % 10, encrypt_key % 10))


def decrypt(text: str, encrypt_key: int):
    return shift_string(text, (-(encrypt_key // 100), -(encrypt_key // 10 % 10), -(encrypt_key % 10)))


def shift_string(text: str, keys: tuple[int, int, int]):
    kb_rows = (
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm,.'
    )
    new_string = ''

    for char in text:
        for i, row in enumerate(kb_rows):
            if char.isupper() or char in '<>':
                row = row.upper().replace(',', '<').replace('.', '>')

            if char in row:
                original_pos = row.index(char)
                new_pos = (original_pos + keys[i]) % len(row)
                new_string += row[new_pos]
                break
        else:
            new_string += char

    return new_string
