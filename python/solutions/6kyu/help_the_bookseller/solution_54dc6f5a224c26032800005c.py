"""https://www.codewars.com/kata/54dc6f5a224c26032800005c"""


def stock_list(stock: list[str], categories: list[str]) -> str:
    if not stock or not categories:
        return ''

    category_counts = {cat: 0 for cat in categories}
    stock = [tuple(s.split()) for s in stock]
    stock = [(s[0], int(n)) for s, n in stock]

    for cat, count in stock:
        if cat in category_counts:
            category_counts[cat] += count

    return ' - '.join(f'({k} : {v})' for k, v in category_counts.items())
