"""https://www.codewars.com/kata/525f47c79f2f25a4db000025"""
import re


def valid_phone_number(phone_number: str):
    return bool(re.search(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number))


def main():
    from util_funcs import pretty_compare

    pretty_compare(valid_phone_number("(123) 456-7890"),        True)
    pretty_compare(valid_phone_number("(1111)555 2345"),        False)
    pretty_compare(valid_phone_number("(098) 123 4567"),        False)
    pretty_compare(valid_phone_number("(123)456-7890"),         False)
    pretty_compare(valid_phone_number("abc(123)456-7890"),      False)
    pretty_compare(valid_phone_number("(123)456-7890abc"),      False)
    pretty_compare(valid_phone_number("abc(123)456-7890abc"),   False)
    pretty_compare(valid_phone_number("abc(123) 456-7890"),     False)
    pretty_compare(valid_phone_number("(123) 456-7890abc"),     False)
    pretty_compare(valid_phone_number("abc(123) 456-7890abc"),  False)
    pretty_compare(valid_phone_number("(333) 185-0594"),        True)


if __name__ == '__main__':
    main()
