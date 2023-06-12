import re


def to_camel_case(text):
    for result in re.findall(r"[-_].", text):
        text = text.replace(result, result[1].upper())
    return text


def to_camel(text):
    return re.sub(r"[-_].", lambda m: m[0][1].upper(), text)


camel = lambda text: re.sub(r"[-_].", lambda m: m[0][1].upper(), text)


if __name__ == '__main__':
    print(to_camel_case("the-stealth-warrior"))
    print(to_camel("the-stealth-warrior"))
    print(camel("the-stealth-warrior"))
