"""https://www.codewars.com/kata/5202ef17a402dd033c000009"""


def title_case(title: str, minor_words=''):
    minor_words = set(minor_words.lower().split())
    words = title.lower().split()
    
    for i, word in enumerate(words):
        if word in minor_words and i != 0:
            continue
        
        words[i] = word.capitalize()
    
    return ' '.join(words)


def main():
    print(title_case(''), '')
    print(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings', sep='\t\t\t')
    print(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows', sep='\t\t')
    print(title_case('the quick brown fox'), 'The Quick Brown Fox', sep='\t\t\t')


if __name__ == '__main__':
    main()

