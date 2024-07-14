from pathlib import Path

import requests

BASE_DIR = Path('./data_extraction/source')

def create_json_data_dir() -> None:
    if Path('./json_data').is_dir():
        return 
    Path('./json_data').mkdir()


def create_gen_dir(gen_index: int) -> None:
    """Checks if the folder exits. If not, it gets created"""
    target_dir = BASE_DIR / f'gen_{gen_index}'
    if target_dir.is_dir():
        return
    target_dir.mkdir()
    print(f'dir created for gen {gen_index}')


def save_pokemon_source_html(pokedex_url: str, gen_index: int, poke_name: str) -> None:
    response = requests.get(pokedex_url)
    file_name = BASE_DIR / f'gen_{gen_index}' / f'{poke_name}.html'
    file_name.touch()
    with open(file=file_name, mode='w', encoding='utf8') as file:
        file.write(response.text)

