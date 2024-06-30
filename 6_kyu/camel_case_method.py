"""https://www.codewars.com/kata/587731fda577b3d1b0001196"""

import re


def camel_case(s: str):
    return re.sub(r'(?:^| )([a-z])', lambda m: m.group(1).upper(), s).strip()


def main():
    print(camel_case("test case"), "TestCase")
    print(camel_case("camel case method"), "CamelCaseMethod")
    print(camel_case("say hello "), "SayHello")
    print(camel_case(" camel case word"), "CamelCaseWord")
    print(camel_case(""), "")


if __name__ == '__main__':
    main()

