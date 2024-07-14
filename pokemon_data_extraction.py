import json
import os
from pathlib import Path

from bs4 import BeautifulSoup

from soup_picker.pokedex_data import get_general_data

# from utils import create_json_data_dir


BASE_PATH = Path('./source')

gens_list = [_ for _ in os.listdir(BASE_PATH) if (BASE_PATH / _).is_dir()]


info = {}

# take gen 1 for testing 
test_gen_dir = BASE_PATH / gens_list[0]
pokemons_source_files = [( test_gen_dir / _) for _ in os.listdir(test_gen_dir) ]

# create_json_data_dir()

with open(file=pokemons_source_files[0], mode='r', encoding='utf8') as file:
    source = file.read()
    soup = BeautifulSoup(source, 'html.parser')
    get_general_data(soup)