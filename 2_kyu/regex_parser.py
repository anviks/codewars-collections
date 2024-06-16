class Normal:
    def __init__(self, char: str):
        self.char = char


class Any:
    pass


class ZeroOrMore:
    def __init__(self, regex):
        self.regex = regex


class Or:
    def __init__(self, regex1, regex2):
        self.regex1 = regex1
        self.regex2 = regex2


class Str:
    def __init__(self, regex_list: list):
        self.regex_list = regex_list
