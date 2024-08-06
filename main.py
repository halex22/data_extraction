import json
from pathlib import Path
from typing import List, Optional

from bs4 import BeautifulSoup

from soup_picker import get_additional_info, get_general_data
from utils.dirs import dir_handler, save_scrapped_info

OUTPUT_DIR = Path('./pokemon json')
INPUT_DIR = Path('./source')


def process_pokemon_info(source_file_path: Path, search_only: Optional[List[str]] = None,
                         exclude_tables: Optional[List[str]] = None, get_add_info: bool = True) -> None:
    """Creates the pokemon dir inside it's generation and saves the info extracted from the html source code of the pokemon

    Args:
        source_file_path (Path): The path to the html source code
        search_only (List[str], optional): Name of the table only table to extract info from, If not given the function will extract all the tables info
        . Defaults to None.
        exclude_tables (List[str], optional): List of tables that will be excluded. Defaults to Optional[List[str]].
    """

    if search_only and exclude_tables:
        raise ValueError(
            'If search_only is not none, exclude_tables must be none')

    tables_name_to_search = exclude_tables if exclude_tables else search_only if search_only else 'all'

    pokemon_output_dir = gen_target / source_file_path.stem

    dir_handler(path_name=pokemon_output_dir)

    # open the source code file
    with open(source_file_path, mode='r', encoding='utf8') as file:
        source_code = file.read()

    soup = BeautifulSoup(source_code, 'html.parser')
    info = get_general_data(soup_instance=soup, tables=tables_name_to_search)

    if get_add_info:
        add_info = get_additional_info(soup=soup)
        info = {**info, **add_info}

    for key, value in info.items():
        save_scrapped_info(destination_dir=pokemon_output_dir,
                           file_name=key, info_section=value)


if __name__ == '__main__':

    dir_handler(OUTPUT_DIR)
    # iterate through the generations dir
    for generation in INPUT_DIR.iterdir():
        gen_index = generation.name[-1]

        print(f'Extracting generation {gen_index} info')
        gen_target = OUTPUT_DIR / f'gen_{gen_index}'
        dir_handler(path_name=gen_target)

        for pokemon_file in generation.iterdir():
            process_pokemon_info(pokemon_file)
