"""https://www.codewars.com/kata/581e014b55f2c52bb00000f8"""

import re


def decipher_this(s: str):
    result = []

    for word in s.split():
        digits = re.search(r'^\d+', word).group()
        m_len = len(digits)
        new_word = chr(int(digits))

        if len(word) < m_len + 2:
            result.append(new_word + word[m_len:])
        else:
            result.append(new_word + word[-1] + word[m_len + 1:-1] + word[m_len])

    return ' '.join(result)


def main():
    print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka") == "A wise old owl lived in an oak")
    print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp") == "The more he saw the less he spoke")
    print(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare") == "The less he spoke the more he heard")
    print(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri") == "Why can we not all be like that wise old bird")
    print(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple") == "Thank you Piotr for all your help")


if __name__ == '__main__':
    main()

