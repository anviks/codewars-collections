"""https://www.codewars.com/kata/54b724efac3d5402db00065e"""

from preloaded import MORSE_CODE

MORSE_CODE[""] = ""


def decode_morse(morse_code: str):
    return " ".join(
        ["".join([MORSE_CODE[letter] for letter in word.split(" ")]) for word in morse_code.split("   ")]).strip()


if __name__ == '__main__':
    print(decode_morse("     .... . -.--   .--- ..- -.. ."))  # "HEY JUDE"
    print(decode_morse('.-'), 'A')
    print(decode_morse('--...'), '7')
    print(decode_morse('...-..-'), '$')
    print(decode_morse('.'), 'E')
    print(decode_morse('..'), 'I')
    print(decode_morse('. .'), 'EE')
    print(decode_morse('.   .'), 'E E')
    print(decode_morse('...-..- ...-..- ...-..-'), '$$$')
    print(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
    print(decode_morse('.-... ---...   -..-. --...'), '&: /7')
    print(decode_morse('...---...'), 'SOS')
    print(decode_morse('... --- ...'), 'SOS')
    print(decode_morse('...   ---   ...'), 'S O S')
    print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
