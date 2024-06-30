"""https://www.codewars.com/kata/simple-encryption-number-2-index-difference"""

from string import ascii_uppercase, ascii_lowercase, digits

REGION = ascii_uppercase + ascii_lowercase + digits + '''.,:;-?! '()$%&"'''


def encrypt(text: str) -> str:
    if not text:
        return text
    
    chars = list(text)
    
    for i, c in enumerate(chars):
        if c not in REGION:
            raise ValueError('Invalid character')
        if i % 2 == 1:
            chars[i] = c.swapcase()
            
    for i in range(len(chars) - 1, 0, -1):
        new_index = (REGION.index(chars[i - 1]) - REGION.index(chars[i]) + len(REGION)) % len(REGION)
        chars[i] = REGION[new_index]
    
    first_index = REGION.index(chars[0])
    chars[0] = REGION[-first_index - 1]

    return ''.join(chars)
    

def decrypt(text: str) -> str:
    if not text:
        return text
    
    chars = list(text)
    
    first_index = REGION.index(chars[0])
    chars[0] = REGION[-first_index - 1]
    
    for i in range(1, len(chars)):
        new_index = (REGION.index(chars[i - 1]) - REGION.index(chars[i]) + len(REGION)) % len(REGION)
        chars[i] = REGION[new_index]
        
    for i, c in enumerate(chars):
        if i % 2 == 1:
            chars[i] = c.swapcase()
            
    return ''.join(chars)
    

def main():
    actual = encrypt("Business")
    expected = "&61kujla"
    print(actual == expected, actual, expected, sep=' ' * 5)

    actual = encrypt("Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!")
    expected = "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"
    print(actual == expected, actual, expected, sep=' ' * 5)

    actual = encrypt("This is a test!")
    expected = "5MyQa9p0riYplZc"
    print(actual == expected, actual, expected, sep=' ' * 5)

    actual = encrypt("This kata is very interesting!")
    expected = "5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p"
    print(actual == expected, actual, expected, sep=' ' * 5)


if __name__ == '__main__':
    main()
