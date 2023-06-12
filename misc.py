import collections


def generate_hashtag(s: str):
    return "#" + s.title().replace(" ", "") if 0 < len(s) < 140 else False


def make_readable(seconds):
    return f"{(rem := divmod(seconds, 3600))[0]:02}:{(rem := divmod(rem[1], 60))[0]:02}:{rem[1]:02}"


def count(s: str):
    return collections.Counter(s)


if __name__ == '__main__':
    # print(generate_hashtag(" Hello there thanks for trying my Kata"))  # "#HelloThereThanksForTryingMyKata"
    # print(generate_hashtag("    Hello     World   "))  # "#HelloWorld"
    # print(generate_hashtag(""))  # False
    # print(generate_hashtag("g" * 141))  # False

    # print(make_readable(0))  # "00:00:00"
    # print(make_readable(5))  # "00:00:05"
    # print(make_readable(60))  # "00:01:00"
    # print(make_readable(86399))  # "23:59:59"
    # print(make_readable(359999))  # "99:59:59"

    print(count("aba"))  # {"a": 2, "b": 1}
    assert count("aba") == {"a": 2, "b": 1}
