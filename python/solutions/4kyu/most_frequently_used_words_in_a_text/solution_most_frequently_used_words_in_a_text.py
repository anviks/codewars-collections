"""https://www.codewars.com/kata/51e056fe544cf36c410000fb"""

import re
from collections import Counter


def top_3_words(text):
    results = re.findall(r"[a-z']+", text.lower())
    results = [res for res in results if set(res) != {"'"}]
    return list((list(zip(*Counter(results).most_common(3))) or [[]])[0])
