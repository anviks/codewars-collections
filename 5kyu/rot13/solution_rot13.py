"""https://www.codewars.com/kata/530e15517bc88ac656000716"""


def rot13(message: str):
    new_msg = ''

    for char in message:
        if char.isupper():
            first_char = 'A'
        elif char.islower():
            first_char = 'a'
        else:
            new_msg += char
            continue

        old_pos = ord(char) - ord(first_char)
        new_pos = (old_pos + 13) % 26 + ord(first_char)
        new_msg += chr(new_pos)

    return new_msg
