import os
from pathlib import Path

import requests

SCRIPT_FILE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


def verify_html_exits(dir_name: str = 'source') -> None:
    target_dir = SCRIPT_FILE_DIR / dir_name
    if not target_dir.is_dir():
        target_dir.mkdir()


def get_source_html_code(url: str = 'https://pokemondb.net/pokedex/national') -> None:
    res = requests.get(url=url)
    file_name = SCRIPT_FILE_DIR / 'source' / 'html_source.html'
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(res.text)



if __name__ == '__main__':
    verify_html_exits()
    get_source_html_code()
# requests.get()
