"""
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

**Regex validate PIN code**

ATMs allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

Examples:
    ``"1234"   -->  True``\n
    ``"12345"  -->  False``\n
    ``"a234"   -->  False``
"""


def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)


if __name__ == '__main__':
    print(validate_pin("1234"))  # True
    print(validate_pin("12345"))  # False
    print(validate_pin("a234"))  # False
    print(validate_pin("0000"))  # True
    print(validate_pin("1111"))  # True
    print(validate_pin("123456"))  # True
