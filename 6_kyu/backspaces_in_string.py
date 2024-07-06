"""https://www.codewars.com/kata/5727bb0fe81185ae62000ae3"""


def clean_string(s: str):
    cleaned = []
    
    for char in s:
        if char == '#':
            cleaned and cleaned.pop()
        else:
            cleaned.append(char)
            
    return ''.join(cleaned)



def main():
    from util_funcs import pretty_compare
    pretty_compare(clean_string('abc#d##c'), 'ac')
    pretty_compare(clean_string('abc####d##c#'), '')
    pretty_compare(clean_string('#######'), '')
    pretty_compare(clean_string(''), '')


if __name__ == '__main__':
    main()
