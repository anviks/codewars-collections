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
                

def main():
    from util_funcs import pretty_compare
    
    pretty_compare(encrypt("A", 111), "S")
    pretty_compare(encrypt("Abc", 212), "Smb")
    pretty_compare(encrypt("Wave", 0), "Wave")  # -> 000
    pretty_compare(encrypt("Wave", 345), "Tg.y")
    pretty_compare(encrypt("Ball", 134), ">fdd")
    pretty_compare(encrypt("Ball", 444), ">gff")
    pretty_compare(encrypt("This is a test.", 348), "Iaqh qh g iyhi,")
    pretty_compare(encrypt("Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.", 583),
          "Sr pgi jlpl Jr,lqlage Zlow Piapc I.skiaa dw. l.s ibnepizi.p ugi. de.se.f l arkwper.c")

    pretty_compare(decrypt("S", 111), "A")
    pretty_compare(decrypt("Smb", 212), "Abc")
    pretty_compare(decrypt("Wave", 0), "Wave")  # -> 000
    pretty_compare(decrypt("Tg.y", 345), "Wave")
    pretty_compare(decrypt(">fdd", 134), "Ball")
    pretty_compare(decrypt(">gff", 444), "Ball")
    pretty_compare(decrypt("Iaqh qh g iyhi,", 348), "This is a test.")
    pretty_compare(decrypt("Sr pgi jlpl Jr,lqlage Zlow Piapc I.skiaa dw. l.s ibnepizi.p ugi. de.se.f l arkwper.c", 583),
          "Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.")


if __name__ == '__main__':
    main()
