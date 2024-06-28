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


def main():
    print(encrypt_this("") == ""),
    print(encrypt_this("A wise old owl lived in an oak") == "65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
    print(encrypt_this("The more he saw the less he spoke") == "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")
    print(encrypt_this("The less he spoke the more he heard") == "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare")
    print(encrypt_this("Why can we not all be like that wise old bird") == "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri")
    print(encrypt_this("Thank you Piotr for all your help") == "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple")


if __name__ == '__main__':
    main()

