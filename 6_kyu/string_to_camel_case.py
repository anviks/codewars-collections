"""
https://www.codewars.com/kata/517abf86da9663f1d2000003

**Convert string to camel case**

Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples:
    "the-stealth-warrior" gets converted to "theStealthWarrior"\n
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"\n
    "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

import re


def to_camel_case(text):
    for result in re.findall(r"[-_].", text):
        text = text.replace(result, result[1].upper())
    return text


def to_camel(text):
    return re.sub(r"[-_].", lambda m: m[0][1].upper(), text)


to_camel_case = lambda text: re.sub(r"[-_].", lambda m: m[0][1].upper(), text)

if __name__ == '__main__':
    print(to_camel_case("the-stealth-warrior"))  # "theStealthWarrior"
    print(to_camel_case("The_Stealth_Warrior"))  # "TheStealthWarrior"
    print(to_camel_case("The_Stealth-Warrior"))  # "TheStealthWarrior"
