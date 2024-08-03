"""https://www.codewars.com/kata/5848565e273af816fb000449"""


def encrypt_this(text: str):
    result = []

    for word in text.split():
        new_word = str(ord(word[0]))
        if len(word) < 3:
            result.append(new_word + word[1:])
        else:
            result.append(new_word + word[-1] + word[2:-1] + word[1])

    return ' '.join(result)
