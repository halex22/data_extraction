import json
import os
from pathlib import Path

from bs4 import BeautifulSoup

from path_generator import create_json_data_dir, create_json_gen_file
from soup_picker.pokedex_data import get_general_data
from utils.misc import get_name_from_file

BASE_PATH = Path('./source')
create_json_data_dir()
# creates an array with the name of all gen (1-9)
gens_list = [_ for _ in os.listdir(BASE_PATH) if (BASE_PATH / _).is_dir()]


# take gen 1 for testing
test_gen_dir = BASE_PATH / gens_list[0]


def get_gen_data(target_gen: Path):

    json_file_path = create_json_gen_file(gen_name=target_gen.name)
   
    pokemons_source_files = [(target_gen / _) for _ in os.listdir(target_gen)]
    info = {}

    for pokemon_file in pokemons_source_files:
        poke_name = get_name_from_file(pokemon_file)
        print(f'getting {poke_name} info...\n')

        with open(file=pokemon_file, mode='r', encoding='utf8') as file:
            source = file.read()
            soup = BeautifulSoup(source, 'html.parser')
            info[poke_name] = get_general_data(soup)

    with open(json_file_path, mode='w', encoding='utf8') as outfile:
        json.dump(info, outfile, ensure_ascii=False)


if __name__ == '__main__':
    for generation in gens_list:
        get_gen_data(BASE_PATH / generation)
