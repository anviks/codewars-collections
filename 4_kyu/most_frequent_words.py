"""https://www.codewars.com/kata/51e056fe544cf36c410000fb"""
import re
from collections import Counter


def top_3_words(text):
    results = re.findall(r"[a-z']+", text.lower())
    results = [res for res in results if set(res) != {"'"}]
    return list((list(zip(*Counter(results).most_common(3))) or [[]])[0])


def main():
    text = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""
    text = "''"
    
    print(top_3_words(text))


if __name__ == '__main__':
    main()

