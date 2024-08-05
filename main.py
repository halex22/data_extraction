import json
from pathlib import Path

from bs4 import BeautifulSoup

from soup_picker import get_general_data
from utils.dirs import dir_handler

OUTPUT_DIR = Path('./pokemon json')
INPUT_DIR = Path('./source')


def save_scrapped_info(destination_dir: Path, file_name: str, info_section: dict):
    target_file = destination_dir / f'{file_name}.json'

    with open(target_file, mode='w', encoding='utf8') as file:
        json.dump(info_section, file, ensure_ascii=False)


def process_pokemon_info(source_file_path: Path) -> None:
    pokemon_output_dir = gen_target / source_file_path.stem
    dir_handler(path_name=pokemon_output_dir)
    print(source_file_path)
    with open(source_file_path, mode='r', encoding='utf8') as file:
        source_code = file.read()
    soup = BeautifulSoup(source_code, 'html.parser')
    info = get_general_data(soup_instance=soup)
    for key, value in info.items():
        # print('\n', key)
        # print(value)
        save_scrapped_info(destination_dir=pokemon_output_dir,
                           file_name=key, info_section=value)


if __name__ == '__main__':

    # iterate through the generations dir
    for generation in INPUT_DIR.iterdir():
        gen_index = generation.name[-1]

        print(f'Extracting generation {gen_index} info')
        gen_target = OUTPUT_DIR / f'gen_{gen_index}'
        dir_handler(path_name=gen_target)

        # for pokemon_file in generation.iterdir():
        #     process_pokemon_info(pokemon_file)

        test_file = next(generation.iterdir().__iter__())
        process_pokemon_info(test_file)
        break  # to test just the first file
