from pathlib import Path
from typing import List

from bs4 import BeautifulSoup, Tag

path_dir = Path('./source/gen_1')

test_set = True


def get_languages(soup: Tag):
    """Finds the languages tables and extracts the data"""
    rows: List[Tag] = soup.find_all('table', attrs={'class': 'vitals-table'})[-1].find_all('tr')
    languages = {}
    for row in rows:
        languages[row.find('th').text] = row.find('td').text
    return languages


if __name__ == '__main__':

    if test_set:

        for _ in path_dir.iterdir():
            print(_)
            with open(_, mode='r', encoding='utf8') as file:
                source_code = file.read()

            soup = BeautifulSoup(source_code, 'html.parser')

            print(get_languages(soup))

    else:
        test_file = next(path_dir.iterdir())

        with open(test_file, mode='r', encoding='utf8') as file:
            source_code = file.read()

        soup = BeautifulSoup(source_code, 'html.parser')

        print(get_languages(soup))
