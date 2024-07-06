import os.path
import re

from bs4 import BeautifulSoup
from requests import get


def main():
    codewars_url = input('Enter the url of a codewars kata you\'re about to solve:\n')
    html = get(codewars_url).text
    soup = BeautifulSoup(html, features='lxml')
    
    kata_title = soup.select_one(r'#shell_content > div.px-0.w-full > div > div.w-full.md\:w-5\/12 > div.flex.items-center > h4').text
    difficulty = soup.select_one(r'#shell_content > div.px-0.w-full > div > div.w-full.md\:w-5\/12 > div.flex.items-center > div > div > span').text
    
    kata_file = '_'.join(re.findall(r'\w+', kata_title.lower())) + '.py'
    directory = difficulty.replace(' ', '_')
    kata_path = os.path.join(directory, kata_file)
    
    if not os.path.exists(directory):
        os.mkdir(directory)

    if os.path.exists(kata_path):
        raise FileExistsError('File for that kata already exists')
    
    with open('template') as r, open(kata_path, 'w') as w:
        w.write(r.read().format(codewars_url=codewars_url))


if __name__ == '__main__':
    main()
