"""
https://www.codewars.com/kata/52449b062fb80683ec000024

**The Hashtag Generator**

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
    - It must start with a hashtag (#).
    - All words must have their first letter capitalized.
    - If the final result is longer than 140 chars it must return false.
    - If the input or the result is an empty string it must return false.

Examples:
    ``" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"``\n
    ``"    Hello     World   "                  =>  "#HelloWorld"``\n
    ``""                                        =>  False``
"""


def generate_hashtag(s):
    return "#" + s.title().replace(" ", "") if 0 < len(s) < 140 else False


if __name__ == '__main__':
    print(generate_hashtag(" Hello there thanks for trying my Kata"))  # "#HelloThereThanksForTryingMyKata"
    print(generate_hashtag("    Hello     World   "))  # "#HelloWorld"
    print(generate_hashtag(""))  # False
    print(generate_hashtag("g" * 200))  # False
    print(generate_hashtag("Do We have A Hashtag"))  # "#DoWeHaveAHashtag"
    print(generate_hashtag("Codewars"))  # "#Codewars"
    print(generate_hashtag("Codewars Is Nice"))  # "#CodewarsIsNice"
    print(generate_hashtag("Codewars is nice"))  # "#CodewarsIsNice"
    print(generate_hashtag("code" + " " * 140 + "wars"))  # False
