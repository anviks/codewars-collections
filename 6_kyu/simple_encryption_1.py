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


def main():
    print(encrypt("This is a test!", 0), "This is a test!")
    print(encrypt("This is a test!", 1), "hsi  etTi sats!")
    print(encrypt("This is a test!", 2), "s eT ashi tist!")
    print(encrypt("This is a test!", 3), " Tah itse sits!")
    print(encrypt("This is a test!", 4), "This is a test!")
    print(encrypt("This is a test!", -1), "This is a test!")
    print(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")
    print()

    print(decrypt("This is a test!", 0), "This is a test!")
    print(decrypt("hsi  etTi sats!", 1), "This is a test!")
    print(decrypt("s eT ashi tist!", 2), "This is a test!")
    print(decrypt(" Tah itse sits!", 3), "This is a test!")
    print(decrypt("This is a test!", 4), "This is a test!")
    print(decrypt("This is a test!", -1), "This is a test!")
    print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")


if __name__ == '__main__':
    main()
