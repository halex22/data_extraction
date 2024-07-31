from pathlib import Path
from typing import List

from bs4 import BeautifulSoup, Tag

path_dir = Path('./source/gen_1')

test_set = False


def get_types_effect(soup: BeautifulSoup) -> str:
    type_effect_dict = {}
    tables: List[Tag] = soup.find_all('table', attrs={'class': 'type-table-pokedex'})
    rows: List[Tag] = tables
    for table in tables:
        rows: List[Tag] = table.find_all('td')
        for row in rows:
            type_name = row.get('title').split(' ')[0].strip().lower()
            effect_cat_name = row.get('title').split('=')[-1].strip()
            type_effect_dict[type_name] = {effect_cat_name: row.text}
    return type_effect_dict


if __name__ == '__main__':

    if test_set:

        for _ in path_dir.iterdir():
            print(_)
            with open(_, mode='r', encoding='utf8') as file:
                source_code = file.read()

            soup = BeautifulSoup(source_code, 'html.parser')

            print(get_types_effect(soup=soup))

    else:
        test_file = next(path_dir.iterdir())

        with open(test_file, mode='r', encoding='utf8') as file:
            source_code = file.read()

        soup = BeautifulSoup(source_code, 'html.parser')

        print(get_types_effect(soup=soup))