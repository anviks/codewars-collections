"""https://www.codewars.com/kata/58708934a44cfccca60000c4"""

FORMATS: dict[str, str] = {
    'F': """<span style="color: pink">{}</span>""",
    'L': """<span style="color: red">{}</span>""",
    'R': """<span style="color: green">{}</span>""",
    'DIGIT': """<span style="color: orange">{}</span>"""
}

def highlight(code):
    grouped: list[list[str]] = [[]]
    result: list[str] = []
    
    for char in code:
        if grouped[-1] and grouped[-1][-1] != char and (not grouped[-1][-1].isdigit() or not char.isdigit()):
            grouped.append([])

        grouped[-1].append(char)
        
    for group in grouped:
        group = ''.join(group)
        if group[0] in 'FLR':
            result.append(FORMATS[group[0]].format(group))
        elif group[0].isdigit():
            result.append(FORMATS['DIGIT'].format(group))
        else:
            result.append(group)
        
    return ''.join(result)


print(highlight("F3RF5LF7"))
print(highlight("FFFR345F2LL"))
