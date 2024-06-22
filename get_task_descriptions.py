import json
import os.path
import re
from requests import get
from bs4 import BeautifulSoup

OVERWRITE_EXISTING_FILES = False
CODEWARS_URL_PATTERN = re.compile(r'(?<=""").*?(https://www\.codewars\.com/kata/\w{24}).*?(?=""")', flags=re.DOTALL)


def main():
    for i in range(1, 8):
        directory = f'{i}_kyu'

        if not os.path.exists(directory):
            continue

        children = os.listdir(directory)
        for child in children:
            filename, extension = os.path.splitext(child)
            md_filename = f'{filename}.md'

            if extension != '.py' or md_filename in children and not OVERWRITE_EXISTING_FILES:
                continue

            with open(f'{directory}/{child}') as f:
                codewars_url_match = CODEWARS_URL_PATTERN.search(f.read())

            if codewars_url_match is None:
                continue

            codewars_url = codewars_url_match.group(1)
            print(codewars_url)
            html = get(codewars_url).text
            soup = BeautifulSoup(html, features='lxml')
            load_event_listener = soup.find_all('script')[-1].text
            data = re.search(r'data: JSON\.parse\("(.*)"\),.*routes: ', load_event_listener, flags=re.DOTALL).group(1)
            remove_escapes = re.sub(r'\\(.)', r'\1', data)
            description = json.loads(remove_escapes)['description']
            description = re.sub(r'```if:python\n(.*?)\n```\n\n?', r'\1', description, flags=re.DOTALL)
            description = re.sub(r'```if:.*?\n.*?\n```\n\n?', '', description, flags=re.DOTALL)

            with open(f'{directory}/{md_filename}', 'w', encoding='utf-8') as f:
                f.write(description)


if __name__ == '__main__':
    main()
